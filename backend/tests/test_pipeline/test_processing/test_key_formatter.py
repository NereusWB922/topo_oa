from app.pipeline.processing.key_formatter import KeyFormatter

import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            {"Key(With)Brackets": "value", "Another (Key) With Brackets": "value"},
            {"key_with_brackets": "value", "another_key_with_brackets": "value"},
        ),
        ({"Outer Key": {"Inner Key": "value"}}, {"outer_key": {"inner_key": "value"}}),
        (
            [{"List Key": "value"}, {"Another List Key": "value"}],
            [{"list_key": "value"}, {"another_list_key": "value"}],
        ),
    ],
)
def test_execute(input, expected):
    formatter = KeyFormatter()
    assert formatter.execute(input) == expected
