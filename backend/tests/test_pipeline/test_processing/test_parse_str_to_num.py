import pytest
from app.pipeline.processing.parse_str_to_num import ParseStrToNum


@pytest.fixture
def parser():
    return ParseStrToNum(target_fields=["field1", "field2.nested"])


@pytest.mark.parametrize(
    "data, expected",
    [
        ({"field1": "123"}, {"field1": 123}),
        ({"field1": None}, {"field1": None}),
        ({"field1": "123.45"}, {"field1": 123.45}),
        ({"field1": "abc"}, {"field1": "abc"}),
        ({"field2": {"nested": "4,560,000"}}, {"field2": {"nested": 4560000}}),
        ({"field1": ["789", "101.11"]}, {"field1": [789, 101.11]}),
        ({"field3": "123"}, {"field3": "123"}),
        (
            {"field1": "123", "field2": {"nested": "456.78"}, "field3": "abc"},
            {"field1": 123, "field2": {"nested": 456.78}, "field3": "abc"},
        ),
    ],
)
def test_parse_str_to_num(parser, data, expected):
    result = parser.execute(data)
    assert result == expected
