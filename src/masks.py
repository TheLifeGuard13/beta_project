import re


def format_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и
    возвращает ее маску в формате XXXX XX** **** XXXX"""
    if number.isdigit() and len(number) == 16:
        list_of_segments = re.findall(".{%s}" % 4, number)
        list_of_segments[1] = list_of_segments[1][:2] + "**"
        list_of_segments[2] = "****"
        return " ".join(list_of_segments)
    else:
        return "Это не номер карты!"


def format_acc_number(number: str) -> str:
    """Функция принимает на вход номер счёта и
    возвращает его маску в формате **XXXX."""
    if number.isdigit() and len(number) == 20:
        return "**" + number[16:]
    else:
        return "Это не номер счета!"
