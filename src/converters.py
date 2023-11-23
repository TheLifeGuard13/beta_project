import json
import typing

import pandas as pd


def load_csv_file(filename: any) -> pd.DataFrame:
    """открывает файл в формате csv и превращает в формат питон"""
    try:
        file_data = pd.read_csv(filename, delimiter=";", encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    return file_data


def load_xlsx_file(filename: str) -> pd.DataFrame:
    """открывает файл в формате xlsx и превращает в формат питон"""
    try:
        file_data = pd.read_excel(filename)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    return file_data


def load_json_file(filename: str) -> typing.Any:
    """открывает файл в формате json и превращает в формат питон"""
    try:
        with open(filename, encoding="utf-8") as file:
            file_data = json.load(file)
    except json.JSONDecodeError:
        file_data = []
    except FileNotFoundError:
        file_data = []
    return file_data
