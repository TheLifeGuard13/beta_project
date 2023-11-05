from src.masks import format_acc_number, format_card_number

import pytest


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("5999414228426353", "5999 41** **** 6353"),
        ("134", "Это не номер карты!"),
    ],
)
def test_format_card_number(string, expected):
    assert format_card_number(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("64686473678894779589", "**9589"),
        ("134", "Это не номер счета!"),
    ],
)
def test_format_acc_number(string, expected):
    assert format_acc_number(string) == expected
