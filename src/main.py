from src.widget import format_payment_info, get_date_from_list

if __name__ == "__main__":
    print(format_payment_info('Maestro 1596837868705199'))
    print(format_payment_info('Счет 64686473678894779589'))
    print(format_payment_info('Visa Gold 5999414228426353'))
    print(format_payment_info('5999414228426353'))
    print(format_payment_info('64686473678894779589'))

    print(get_date_from_list('2018-07-11T02:26:18.671407'))