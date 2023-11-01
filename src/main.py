from src.processing import get_formatted_list, get_formatted_list_by_date
from src.widget import format_payment_info, get_date_from_list

input_dictionary = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    # ДОМАШНЕЕ ЗАДАНИЕ №1
    print(format_payment_info("Maestro 1596837868705199"))
    print(format_payment_info("Счет 64686473678894779589"))
    print(format_payment_info("Visa Gold 5999414228426353"))
    print(format_payment_info("5999414228426353"))
    print(format_payment_info("64686473678894779589"))

    print(get_date_from_list("2018-07-11T02:26:18.671407"))

    # Задание 1. Проект (ДОМАШНЕЕ ЗАДАНИЕ №2)
    print(get_formatted_list(input_dictionary, "EXECUTED"))
    print(get_formatted_list_by_date(input_dictionary))
    print(get_formatted_list_by_date(input_dictionary, False))
