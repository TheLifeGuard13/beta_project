from src.masks import format_acc_number, format_card_number


def test_format_card_number():
    assert format_card_number("1596837868705199") == "1596 83** **** 5199"
    assert format_card_number("") == "Это не номер карты!"


def test_format_acc_number():
    assert format_acc_number("64686473678894779589") == "**9589"
    assert format_acc_number("") == "Это не номер счета!"
