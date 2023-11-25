import re


def get_formatted_list(any_list: list[dict], status: str = "") -> list[dict]:
    """выбирает из списка словарей, словари с определенным значением (задается вторым аргументом)"""
    new_list = []
    for one_dict in any_list:
        if one_dict["state"] == status:
            new_list.append(one_dict)
    return new_list


def get_formatted_list_by_date(any_list: list[dict], sort_up: bool = True) -> list[dict]:
    """упорядочивает словари по дате (со вторым параметром сортировка от меньшей к большей и наоборот)"""
    if sort_up:
        sorted_list = sorted(any_list, key=lambda x: x["date"])
    else:
        sorted_list = sorted(any_list, key=lambda x: x["date"], reverse=True)
    return sorted_list


def find_operation_by_description(any_list: list[dict], description: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска и
    возвращает список словарей, у которых в описании есть данная строка"""
    return [x for x in any_list if x if re.search(description, x["description"], flags=re.I)]


def find_categories(any_list: list[dict], category: dict) -> dict:
    """принимать список словарей с данными о банковских операциях и словарь категорий операций
    и возвращать словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории."""
    cat_list = [value for key, value in category.items()]
    dict_ = {}
    for cat in cat_list:
        dict_[cat] = len([x for x in any_list if x if re.search(cat, x["description"], flags=re.I)])
    return dict_
