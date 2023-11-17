import logging
import os
import re
from pathlib import Path

DATA_PATH_LOG = Path(__file__).parent.parent.joinpath("data", "masks_log.txt")
logger = logging.getLogger("__masks__")

if os.path.exists(DATA_PATH_LOG):
    os.remove(DATA_PATH_LOG)

file_handler = logging.FileHandler(DATA_PATH_LOG)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def format_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и
    возвращает ее маску в формате XXXX XX** **** XXXX"""
    if number.isdigit() and len(number) == 16:
        list_of_segments = re.findall(".{%s}" % 4, number)
        list_of_segments[1] = list_of_segments[1][:2] + "**"
        list_of_segments[2] = "****"
        logger.info("Card number OK")
        return " ".join(list_of_segments)
    else:
        logger.info("Wrong card number input")
        return "Это не номер карты!"


def format_acc_number(number: str) -> str:
    """Функция принимает на вход номер счёта и
    возвращает его маску в формате **XXXX."""
    if number.isdigit() and len(number) == 20:
        logger.info("Acc number OK")
        return "**" + number[16:]
    else:
        logger.info("Wrong acc number input")
        return "Это не номер счета!"


# print(format_card_number("1234567890123456"))
# print(format_card_number("111"))
# print(format_acc_number("12345678901234567890"))
# print(format_acc_number("222"))
