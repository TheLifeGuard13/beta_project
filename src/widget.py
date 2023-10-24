import re


def format_payment_info(info: str) -> str:
    """принимает на вход строку с информацией тип и номер карты/счета
    и возвращает эту строку с замаскированным номером карты/счета
    в формате XXXX XX** **** XXXX для карты и
    в формате **XXXX для счета."""
    list_of_info = info.split(' ')
    payment_number = list_of_info.pop()
    payment_type = ' '.join(list_of_info)
    if payment_type == '' and len(payment_number) == 16:
        payment_type = 'AnyCard'
    elif payment_type == '' and len(payment_number) == 20:
        payment_type = 'Счет'
    if payment_number.isdigit() and len(payment_number) == 16:
        list_of_segments = re.findall(".{%s}" % 4, payment_number)
        list_of_segments[1] = list_of_segments[1][:2] + "**"
        list_of_segments[2] = "****"
        return f'{payment_type} {" ".join(list_of_segments)}'
    elif payment_number.isdigit() and len(payment_number) == 20:
        return f'{payment_type} {"**" + payment_number[16:]}'
    else:
        return "Это не номер карты/счета!"


def get_date_from_list(string: str) -> str:
    """принимает на вход строку, вида '2018-07-11T02:26:18.671407'
    и возвращает строку с датой в виде '11.07.2018'"""
    date_old_string = string.split('T')[0]
    date = date_old_string.split('-')[2]
    month = date_old_string.split('-')[1]
    year = date_old_string.split('-')[0]
    return f'{date}.{month}.{year}'
