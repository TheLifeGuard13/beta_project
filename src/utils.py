import json
import random
import typing


def load_file(filename: str) -> typing.Any:
    """открывает файл со списком словарей в формате json и превращает в формат питон"""
    try:
        with open(filename, encoding="utf-8") as file:
            file_data = json.load(file)
    except json.JSONDecodeError:
        file_data = []
    except FileNotFoundError:
        file_data = []
    return file_data


def pick_one_operation(operations: list[dict]) -> dict:
    """выбирает случайную транзакцию из списка операций"""
    return random.choice(operations)


def check_currency(operation: dict) -> float:
    """вычисляет сумму транзакции в рублях или выдает ошибку, если валюта - не рубли"""
    if operation:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    else:
        raise Exception("Транзакция не найдена")
