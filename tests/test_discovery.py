from tools.discover import discover
from tools.generate import render
from tools.observe_types import omit_required
from tools.type_info import apply_observations, expression_schema, field_schemas, python_type


def test_parser_handles_inheritance_dynamic_tables_and_callbacks():
    source = b"""
    var x = class {controller; role;};
    var A = class extends x {role="main";controller="GetURLInfoWS";};
    var B = class extends x {role="main";controller="FetchTableWS";};
    var base = class {
      static fetch(){const q={url:location.pathname,dataType:3,params:this.g189(),limit:5,offset:0};
        new this.factory(q, callback);}
    };
    var table = class extends base { static factory=B;
      static g189(){return {userId:user.id,country:""};}
      static g190(){return rank("score");}
    };
    new A({userId:1, extra:!1},({user: u})=>render(u));
    var EventClass = class {name="NewMessageEvent";};
    """
    result = discover(source, 1234)
    assert result["events"] == ["NewMessageEvent"]
    info = next(a for a in result["apis"] if a["controller"] == "GetURLInfoWS")
    assert info["method"] == "get_url_info"
    assert info["observed_response_fields"] == ["user"]
    assert info["observed_requests"][0]["literals"] == {"userId": 1, "extra": False}
    assert info["request_schema"]["properties"]["userId"] == {"type": "integer"}
    assert info["request_schema"]["properties"]["extra"] == {"type": "boolean"}
    assert info["response_schema"]["properties"]["user"] == {}
    table = next(a for a in result["apis"] if a["controller"] == "FetchTableWS")
    assert table["table_query_fields"] == [["country", "userId"]]
    assert table["table_sorts"] == ["score"]
    assert table["request_schema"]["properties"]["params"]["properties"]["country"] == {
        "type": "string",
    }
    generated = render(result)
    assert any("async def get_url_info" in text for text in generated.values())


def test_parser_refuses_invalid_bundle():
    import pytest

    with pytest.raises(ValueError):
        discover(b"var broken = class {", 1)


def test_syntax_types_do_not_guess_dynamic_values():
    import tree_sitter_javascript
    from tree_sitter import Language, Parser

    source = b"""const payload={
        id:parseInt(input), flag:!!input, ratio:Math.random(), name:String(input),
        optional:condition ? "value" : null, unknown:helper(input),
        values:[1,"text",true], empty:[], dynamic:[helper(input)],
        comparison: a===b, integer: 123, decimal: 1.5,
    };"""
    tree = Parser(Language(tree_sitter_javascript.language())).parse(source)
    expr = tree.root_node.named_children[0].named_children[0].child_by_field_name("value")
    properties = expression_schema(expr)["properties"]
    assert python_type(properties["id"]) == "int"
    assert python_type(properties["flag"]) == "bool"
    assert python_type(properties["ratio"]) == "int | float"
    assert python_type(properties["name"]) == "str"
    assert python_type(properties["optional"]) == "str | None"
    assert python_type(properties["unknown"]) == "JsonValue"
    assert python_type(properties["empty"]) == "list[JsonValue]"
    assert python_type(properties["dynamic"]) == "list[JsonValue]"
    assert python_type(properties["values"]) == "list[bool | int | str]"
    assert python_type(properties["comparison"]) == "bool"
    assert python_type(properties["integer"]) == "int"
    assert python_type(properties["decimal"]) == "int | float"


def test_live_types_merge_nullable_nested_fields_and_render_evidence():
    source = b"""var A=class{role="main";controller="GetInfoWS";};
        new A({id:1},({result})=>render(result));"""
    catalog = discover(source, 1)
    response = {
        "type": "object",
        "properties": {
            "result": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": ["string", "null"]},
                        "id": {"type": "integer"},
                    },
                },
            },
            "notResolved": {},
            "nullOnly": {"type": "null"},
        },
    }
    apply_observations(
        catalog,
        {
            "version": 1,
            "source_sha256": catalog["sha256"],
            "apis": {"GetInfoWS": {"response": response}},
        },
    )
    api = catalog["apis"][0]
    fields = dict(field_schemas(api["response_schema"]))
    assert python_type(fields["result[].username"]) == "str | None"
    assert api["response_type_sources"]["result[].id"] == ["live sample"]
    docs = next(text for path, text in render(catalog).items() if path.name == "endpoints.md")
    assert "| `result[].username` | `str \\| None` | live sample |" in docs
    assert "| `notResolved` | `JsonValue` | unresolved |" in docs
    assert "only null observed" in docs


def test_type_evidence_requires_matching_version_and_source_hash():
    import pytest

    catalog = discover(b'var A=class{role="main";controller="GetInfoWS";};', 1)
    with pytest.raises(ValueError, match="version"):
        apply_observations(catalog, {"version": 2})
    with pytest.raises(ValueError, match="bundle"):
        apply_observations(catalog, {"version": 1, "source_sha256": "wrong"})


def test_removing_sample_requiredness_preserves_a_field_called_required():
    schema = {
        "type": "object",
        "required": ["required"],
        "properties": {
            "required": {"type": "boolean"},
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["x"],
                    "properties": {"x": {"type": "integer"}},
                },
            },
        },
    }
    result = omit_required(schema)
    assert "required" not in result
    assert result["properties"]["required"] == {"type": "boolean"}
    assert "required" not in result["properties"]["items"]["items"]
