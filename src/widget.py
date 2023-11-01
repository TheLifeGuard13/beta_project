from src.masks import format_acc_number, format_card_number


def format_payment_info(info: str) -> str:
    """принимает на вход строку с информацией тип и номер карты/счета
    и возвращает эту строку с замаскированным номером карты/счета
    в формате XXXX XX** **** XXXX для карты и
    в формате **XXXX для счета."""
    list_of_info = info.split(" ")
    payment_number = list_of_info.pop()
    payment_type = " ".join(list_of_info)

    if payment_number.isdigit() and len(payment_number) == 16:
        card_number = format_card_number(payment_number)
        return f"{payment_type} {card_number}"
    elif payment_number.isdigit() and len(payment_number) == 20:
        acc_number = format_acc_number(payment_number)
        return f"{payment_type} {acc_number}"
    else:
        return "Это не номер карты/счета!"


def get_date_from_list(string: str) -> str:
    """принимает на вход строку, вида '2018-07-11T02:26:18.671407'
    и возвращает строку с датой в виде '11.07.2018'"""
    date_old_string = string.split("T")[0]
    date = date_old_string.split("-")[2]
    month = date_old_string.split("-")[1]
    year = date_old_string.split("-")[0]
    return f"{date}.{month}.{year}"
