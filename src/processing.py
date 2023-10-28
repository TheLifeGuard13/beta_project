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
