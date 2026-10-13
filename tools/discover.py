"""Extract API metadata from the public bundle without executing JavaScript.

Install the research extra before running this tool. Download the current
index-NNNN.js from the site's home page, then pass its local path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import tree_sitter_javascript
from tree_sitter import Language, Node, Parser

if __package__:
    from .type_info import add_schema, apply_observations, expression_schema
else:
    from type_info import add_schema, apply_observations, expression_schema


def walk(node: Node):
    yield node
    for child in node.named_children:
        yield from walk(child)


def value(node: Node | None):
    if node is None:
        return None
    raw = node.text.decode()
    if node.type == "string":
        return raw[1:-1]
    if raw in ("!0", "true"):
        return True
    if raw in ("!1", "false"):
        return False
    if raw == "null":
        return None
    if node.type == "number":
        try:
            result = float(raw)
            return int(result) if result.is_integer() else result
        except ValueError:
            return None
    return None


def fields(node: Node | None) -> list[str]:
    if node is None or node.type not in ("object", "object_pattern"):
        return []
    result = []
    for child in node.named_children:
        key = child.child_by_field_name("key")
        if key is not None:
            result.append(key.text.decode().strip("\"'"))
        elif child.type.startswith("shorthand_property_identifier"):
            result.append(child.text.decode())
    return sorted(set(result))


def snake(name: str) -> str:
    name = re.sub(r"WS$", "", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def discover(source: bytes, version: int) -> dict:
    tree = Parser(Language(tree_sitter_javascript.language())).parse(source)
    if tree.root_node.has_error:
        raise ValueError("JavaScript parse failed; do not generate a partial catalogue")
    nodes = list(walk(tree.root_node))
    apis = {}
    symbols = {}
    events = set()
    for node in nodes:
        if node.type != "variable_declarator":
            continue
        cls = node.child_by_field_name("value")
        if cls is None or cls.type != "class":
            continue
        body = cls.child_by_field_name("body")
        props = {
            c.child_by_field_name("property").text.decode(): value(c.child_by_field_name("value"))
            for c in body.named_children
            if c.type == "field_definition" and c.child_by_field_name("property") is not None
        }
        if isinstance(props.get("name"), str) and props["name"].endswith("Event"):
            events.add(props["name"])
        if not isinstance(props.get("controller"), str):
            continue
        controller = props["controller"]
        name = node.child_by_field_name("name").text.decode()
        symbols[name] = controller
        apis[controller] = {
            "controller": controller,
            "method": snake(controller),
            "role": props["role"],
            "skip_rate_limit": props.get("skipRateLimit", False),
            "limited_functionality": props.get("limitedFunctionality", False),
            "closes_session": props.get("closesSession", False),
            "source_offset": cls.start_byte,
            "observed_requests": [],
            "observed_response_fields": [],
            "call_sites": 0,
            "table_query_fields": [],
            "table_sorts": [],
            "request_schema": {},
            "response_schema": {},
            "request_type_sources": {},
            "response_type_sources": {},
        }
    # Resolve the browser's inherited table factory, rather than overlooking
    # controllers called through `new this.<field>(...)`.
    classes = {}
    factories = {}
    for node in nodes:
        if node.type != "variable_declarator":
            continue
        cls = node.child_by_field_name("value")
        if cls is None or cls.type != "class":
            continue
        symbol = node.child_by_field_name("name").text.decode()
        classes[symbol] = cls
        for item in walk(cls):
            if item.type != "new_expression":
                continue
            target = item.child_by_field_name("constructor")
            if target is not None and target.type == "member_expression":
                obj = target.child_by_field_name("object")
                prop = target.child_by_field_name("property")
                if obj is not None and obj.type == "this" and prop is not None:
                    factories[symbol] = prop.text.decode()
    for cls in classes.values():
        heritage = next((n for n in cls.named_children if n.type == "class_heritage"), None)
        if heritage is None or not heritage.named_children:
            continue
        parent = heritage.named_children[0].text.decode()
        factory_field = factories.get(parent)
        if factory_field is None:
            continue
        body = cls.child_by_field_name("body")
        for member in body.named_children:
            if member.type != "field_definition":
                continue
            key = member.child_by_field_name("property")
            target = member.child_by_field_name("value")
            if key is None or target is None or key.text.decode() != factory_field:
                continue
            controller = symbols.get(target.text.decode())
            if controller is None:
                continue
            api = apis[controller]
            base = classes[parent]
            for obj in walk(base):
                if obj.type == "object" and "dataType" in fields(obj):
                    literals = {}
                    for pair in obj.named_children:
                        k = pair.child_by_field_name("key")
                        v = pair.child_by_field_name("value")
                        if k and v and v.type == "number":
                            literals[k.text.decode()] = value(v)
                    shape = {"fields": fields(obj), "literals": literals}
                    if shape not in api["observed_requests"]:
                        api["observed_requests"].append(shape)
                    add_schema(api, "request", expression_schema(obj), "frontend syntax")
            for method in body.named_children:
                name = method.child_by_field_name("name")
                if method.type != "method_definition" or name is None:
                    continue
                if name.text == b"g189":
                    for ret in walk(method):
                        if ret.type == "return_statement" and ret.named_children:
                            shape = fields(ret.named_children[0])
                            if shape and shape not in api["table_query_fields"]:
                                api["table_query_fields"].append(shape)
                            if shape:
                                add_schema(
                                    api,
                                    "request",
                                    {
                                        "type": "object",
                                        "properties": {
                                            "params": expression_schema(ret.named_children[0]),
                                        },
                                    },
                                    "frontend syntax",
                                )
                if name.text == b"g190":
                    for call in walk(method):
                        if call.type == "call_expression":
                            args = call.child_by_field_name("arguments")
                            if (
                                args
                                and args.named_children
                                and args.named_children[0].type == "string"
                            ):
                                sort = value(args.named_children[0])
                                if sort not in api["table_sorts"]:
                                    api["table_sorts"].append(sort)
            api["observed_response_fields"] = ["count", "initData", "position", "rows", "url"]
            add_schema(
                api,
                "response",
                {
                    "type": "object",
                    "properties": {key: {} for key in api["observed_response_fields"]},
                },
                "frontend syntax",
            )
    for node in nodes:
        if node.type != "new_expression":
            continue
        constructor = node.child_by_field_name("constructor")
        if constructor is None or constructor.text.decode() not in symbols:
            continue
        api = apis[symbols[constructor.text.decode()]]
        api["call_sites"] += 1
        arguments = node.child_by_field_name("arguments")
        args = arguments.named_children if arguments else []
        if not args:
            add_schema(api, "request", {"type": "null"}, "frontend syntax")
            continue
        payload = args[0]
        if payload.type in ("arrow_function", "function_expression"):
            add_schema(api, "request", {"type": "null"}, "frontend syntax")
        if payload.type == "identifier":
            # Resolve a local object variable within the containing function.
            scope = node.parent
            while scope and scope.type not in (
                "method_definition",
                "arrow_function",
                "function_declaration",
            ):
                scope = scope.parent
            if scope:
                declarations = [
                    n
                    for n in walk(scope)
                    if n.type == "variable_declarator"
                    and n.start_byte < node.start_byte
                    and n.child_by_field_name("name").text == payload.text
                ]
                if declarations:
                    payload = declarations[-1].child_by_field_name("value")
        keys = fields(payload)
        if keys:
            add_schema(api, "request", expression_schema(payload), "frontend syntax")
            literals = {}
            for pair in payload.named_children:
                k = pair.child_by_field_name("key")
                v = pair.child_by_field_name("value")
                if (
                    k
                    and v
                    and (
                        v.type in ("number", "string", "true", "false", "null")
                        or v.text in (b"!0", b"!1")
                    )
                ):
                    literals[k.text.decode().strip("\"'")] = value(v)
            shape = {"fields": keys, "literals": literals}
            if shape not in api["observed_requests"]:
                api["observed_requests"].append(shape)
        callbacks = [a for a in args if a.type == "arrow_function"]
        for callback in callbacks:
            params = callback.child_by_field_name("parameters")
            if params:
                for param in params.named_children:
                    api["observed_response_fields"] += fields(param)
                    if fields(param):
                        add_schema(api, "response", expression_schema(param), "frontend syntax")
        api["observed_response_fields"] = sorted(set(api["observed_response_fields"]))
    if not apis:
        raise ValueError("No controllers found")
    if len({a["method"] for a in apis.values()}) != len(apis):
        raise ValueError("Python method name collision")
    return {
        "version": version,
        "source_url": f"https://minesweeper.online/js/index-{version}.js",
        "sha256": hashlib.sha256(source).hexdigest(),
        "apis": sorted(apis.values(), key=lambda a: a["controller"]),
        "events": sorted(events),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--version", type=int, required=True)
    parser.add_argument("--output", type=Path, default=Path("src/wom_api/api_catalog.json"))
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--observations", type=Path, help="Reviewed live type-only observations for this bundle"
    )
    args = parser.parse_args()
    catalog = discover(args.bundle.read_bytes(), args.version)
    if args.observations:
        apply_observations(catalog, json.loads(args.observations.read_text(encoding="utf-8")))
    result = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if args.output.read_text(encoding="utf-8") != result:
            raise SystemExit("Catalogue differs; review protocol changes before updating")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    print(f"Discovered {len(json.loads(result)['apis'])} APIs")


if __name__ == "__main__":
    main()
