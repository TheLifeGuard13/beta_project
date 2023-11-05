import pytest

from src.widget import format_payment_info, get_date_from_list


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("134", "Это не номер карты/счета!"),
    ],
)
def test_format_payment_info(string, expected):
    assert format_payment_info(string) == expected


def test_get_date_from_list():
    assert get_date_from_list("2018-07-11T02:26:18.671407") == "11.07.2018"
