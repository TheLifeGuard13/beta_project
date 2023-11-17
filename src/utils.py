import json
import logging
import os
import random
import typing
from pathlib import Path

from config import DATA_PATH_TEST, DATA_PATH_TEST2

DATA_PATH_LOG = Path(__file__).parent.parent.joinpath("data", "utils_log.txt")
logger = logging.getLogger("__utils__")

if os.path.exists(DATA_PATH_LOG):
    os.remove(DATA_PATH_LOG)

file_handler = logging.FileHandler(DATA_PATH_LOG)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def load_file(filename: str) -> typing.Any:
    """открывает файл со списком словарей в формате json и превращает в формат питон"""
    try:
        with open(filename, encoding="utf-8") as file:
            file_data = json.load(file)
            logger.info("JSON OK")
    except json.JSONDecodeError:
        logger.info("JSONDecodeError")
        file_data = []
    except FileNotFoundError:
        logger.info("FileNotFoundError")
        file_data = []
    return file_data


def pick_one_operation(operations: list[dict]) -> dict:
    """выбирает случайную транзакцию из списка операций"""
    logger.info("pick one OK")
    return random.choice(operations)


def check_currency(operation: dict) -> float:
    """вычисляет сумму транзакции в рублях или выдает ошибку, если валюта - не рубли"""
    if operation:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Currency OK")
            return float(operation["operationAmount"]["amount"])
        else:
            logger.info("Wrong currency")
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    else:
        logger.info("Operation not found")
        raise Exception("Транзакция не найдена")


# print(load_file(DATA_PATH_TEST))    # [dict, dict ...]
# print(load_file(DATA_PATH_TEST2))  # []
# print(load_file("./src/test_json.json"))  # []

# print(pick_one_operation(load_file(DATA_PATH_TEST)))  #

# print(check_currency({'operationAmount': {'currency': {'code': 0}}}))  #
# print(check_currency({'operationAmount': {'currency': {'code': 'RUB'}}}))  #
# print(check_currency({}))  #
