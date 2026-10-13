"""Conservative syntax observations and JSON Schema-based type documentation.

GenSON merges JSON type observations. These schemas describe observations, not
validation contracts; dynamic JavaScript expressions deliberately stay unknown.
"""

from __future__ import annotations

from collections.abc import Iterator

from genson import SchemaBuilder
from tree_sitter import Node


def merge_schema(*schemas: dict) -> dict:
    builder = SchemaBuilder(schema_uri=None)
    for schema in schemas:
        builder.add_schema(schema)
    return builder.to_schema()


def expression_schema(node: Node | None) -> dict:
    if node is None:
        return {}
    if node.type in ("string", "template_string"):
        return {"type": "string"}
    if node.type in ("true", "false"):
        return {"type": "boolean"}
    if node.type == "null":
        return {"type": "null"}
    if node.type == "number":
        try:
            number = float(node.text.decode())
            return {"type": "integer" if number.is_integer() else "number"}
        except ValueError:
            return {}
    if node.type in ("object", "object_pattern"):
        properties = {}
        for child in node.named_children:
            key = child.child_by_field_name("key")
            if key is not None and key.type != "computed_property_name":
                properties[key.text.decode().strip("\"'")] = (
                    expression_schema(child.child_by_field_name("value"))
                    if node.type == "object"
                    else {}
                )
            elif child.type.startswith("shorthand_property_identifier"):
                properties[child.text.decode()] = {}
        return {"type": "object", "properties": properties}
    if node.type == "array":
        items = [expression_schema(child) for child in node.named_children]
        # An unknown element or spread prevents a reliable element type.
        schema = merge_schema(*items) if items and all(items) else {}
        return {"type": "array", "items": schema}
    if node.type == "parenthesized_expression":
        return expression_schema(node.named_children[0])
    if node.type == "ternary_expression":
        yes = expression_schema(node.child_by_field_name("consequence"))
        no = expression_schema(node.child_by_field_name("alternative"))
        return merge_schema(yes, no) if yes and no else {}
    if node.type == "unary_expression":
        operator = node.child_by_field_name("operator")
        arg = node.child_by_field_name("argument")
        op = operator.text.decode() if operator else ""
        if op == "!":
            return {"type": "boolean"}
        if op == "typeof":
            return {"type": "string"}
        if op == "~":
            return {"type": "integer"}
        if op in ("+", "-"):
            known = expression_schema(arg)
            return known if known.get("type") == "integer" else {"type": "number"}
    if node.type == "binary_expression":
        operator = node.child_by_field_name("operator")
        op = operator.text.decode() if operator else ""
        if op in ("==", "!=", "===", "!==", "<", ">", "<=", ">=", "in", "instanceof"):
            return {"type": "boolean"}
        if op in ("|", "&", "^", "<<", ">>", ">>>"):
            return {"type": "integer"}
        if op in ("-", "*", "/", "%", "**"):
            return {"type": "number"}
        if op == "+":
            left = expression_schema(node.child_by_field_name("left"))
            right = expression_schema(node.child_by_field_name("right"))
            if "string" in (left.get("type"), right.get("type")):
                return {"type": "string"}
            if left.get("type") in ("integer", "number") and right.get("type") in (
                "integer",
                "number",
            ):
                return {"type": "number"}
    if node.type == "member_expression" and node.text in (
        b"location.pathname",
        b"location.hostname",
        b"location.hash",
    ):
        return {"type": "string"}
    if node.type == "call_expression":
        target = node.child_by_field_name("function")
        if target is None:
            return {}
        name = target.text.decode()
        if name in ("parseInt", "Number.parseInt", "Date.now"):
            return {"type": "integer"}
        if name in ("parseFloat", "Number.parseFloat", "Number", "Math.random"):
            return {"type": "number"}
        if name == "Boolean":
            return {"type": "boolean"}
        if name == "String":
            return {"type": "string"}
        if name in ("Math.floor", "Math.ceil", "Math.round", "Math.trunc", "Math.imul"):
            return {"type": "integer"}
        if name.startswith("Math."):
            return {"type": "number"}
        # Avoid inferring arbitrary methods on dynamic values (e.g. .val()).
    return {}


def field_schemas(schema: dict, prefix: str = "") -> Iterator[tuple[str, dict]]:
    """Flatten object properties and array items into readable field paths."""
    children = {}
    branches = [schema, *schema.get("anyOf", [])]
    for branch in branches:
        for name, child in branch.get("properties", {}).items():
            path = f"{prefix}.{name}" if prefix else name
            children[path] = merge_schema(children.get(path, {}), child)
        if "items" in branch:
            path = prefix + "[]"
            children[path] = merge_schema(children.get(path, {}), branch["items"])
    for path, child in sorted(children.items()):
        yield path, child
        yield from field_schemas(child, path)


def python_type(schema: dict) -> str:
    types = schema.get("type", [])
    if isinstance(types, str):
        types = [types]
    parts = set()
    for kind in types:
        if kind == "array":
            parts.add(f"list[{python_type(schema.get('items', {}))}]")
        else:
            parts.add(
                {
                    "null": "None",
                    "boolean": "bool",
                    "integer": "int",
                    "number": "int | float",
                    "string": "str",
                    "object": "dict[str, JsonValue]",
                }[kind]
            )
    for variant in schema.get("anyOf", []):
        parts.add(python_type(variant))
    # A number observation subsumes integers in JSON Schema's numeric model.
    if "int | float" in parts:
        parts.discard("int")
    if not parts or "JsonValue" in parts:
        return "JsonValue"
    return " | ".join(sorted(parts, key=lambda part: (part == "None", part)))


def add_schema(api: dict, direction: str, schema: dict, evidence: str) -> None:
    key = f"{direction}_schema"
    api[key] = merge_schema(api.get(key, {}), schema)
    sources = api.setdefault(f"{direction}_type_sources", {})
    for path, field in [("$", schema), *field_schemas(schema)]:
        if field:
            sources[path] = sorted(set([*sources.get(path, []), evidence]))


def apply_observations(catalog: dict, observations: dict) -> None:
    """Apply reviewed live type-only metadata to the matching browser version."""
    if observations["version"] != catalog["version"]:
        raise ValueError("Type observations refer to a different frontend version")
    if observations["source_sha256"] != catalog["sha256"]:
        raise ValueError("Type observations refer to a different frontend bundle")
    apis = {api["controller"]: api for api in catalog["apis"]}
    for controller, observed in observations["apis"].items():
        if controller not in apis:
            raise ValueError(f"Unknown observed controller: {controller}")
        for direction in ("request", "response"):
            if direction in observed:
                add_schema(apis[controller], direction, observed[direction], "live sample")
        apis[controller]["observed_response_fields"] = sorted(
            set(
                [
                    *apis[controller]["observed_response_fields"],
                    *observed.get("response", {}).get("properties", {}),
                ]
            )
        )
