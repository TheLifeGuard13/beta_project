import re
import typing


def filter_by_currency(list_of_transactions: list[dict], currency: str) -> typing.Generator:
    """Принимает список словарей и строку,
    и возвращает итератор, который выдает по очереди id операции,
    в которых указана заданная валюта."""
    for i in filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, list_of_transactions):
        yield i


def transaction_descriptions(list_of_transactions: list[dict]) -> typing.Generator:
    """генератор, который принимает список словарей и возвращает
    описание каждой операции по очереди."""
    for i in list_of_transactions:
        yield i["description"]


def card_number_generator(start: int, finish: int) -> typing.Generator:
    """генератор номеров банковских карт в формате "XXXX XXXX XXXX XXXX"
    в заданном диапазоне, которые передаются как параметры)."""
    if 0 < start <= 9999_9999_9999_9999 or 0 < finish <= 9999_9999_9999_9999:
        y = (str(x).zfill(16) for x in range(start, finish + 1))
        for i in y:
            yield " ".join(re.findall(".{%s}" % 4, i))
    else:
        return "Задайте не более 16 цифр"
