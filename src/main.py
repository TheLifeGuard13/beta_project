from src.hw_add_tasks import get_format_string, get_nums_multiple
from src.widget import format_payment_info, get_date_from_list

if __name__ == "__main__":
    print(format_payment_info("Maestro 1596837868705199"))
    print(format_payment_info("Счет 64686473678894779589"))
    print(format_payment_info("Visa Gold 5999414228426353"))
    print(format_payment_info("5999414228426353"))
    print(format_payment_info("64686473678894779589"))

    print(get_date_from_list("2018-07-11T02:26:18.671407"))
    # дополнительное задание №1
    print(get_format_string(["hello", "world", "apple", "pear", "banana", "pop"]))
    print(get_format_string(["", "madam", "racecar", "noon", "level", ""]))
    print(get_format_string([]))
    # дополнительное задание №2
    print(get_nums_multiple([2, 3, 5, 7, 11]))
    print(get_nums_multiple([-5, -7, -9, -13]))
    print(get_nums_multiple([1, 2]))
    print(get_nums_multiple([4]))
