import pytest

from config import DATA_PATH, DATA_PATH_TEST3
from src.converters import load_json_file
from src.processing import (find_categories, find_operation_by_description, get_formatted_list,
                            get_formatted_list_by_date)

operations = load_json_file(DATA_PATH)
wrong_operations = load_json_file(DATA_PATH_TEST3)
dict__ = {
    1: "Перевод организации",
    2: "Перевод со счета на счет",
    3: "Перевод с карты на карту",
    4: "Открытие вклада",
    5: "Перевод с карты на счет",
}


@pytest.fixture
def operations_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_get_formatted_list_by_status(operations_list):
    assert get_formatted_list(operations_list, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_get_formatted_list_by_date(operations_list):
    assert get_formatted_list_by_date(operations_list) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_get_formatted_list_by_date2(operations_list):
    assert get_formatted_list_by_date(operations_list, False) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_find_operation_by_description():
    assert find_operation_by_description(operations, "Открытие вклада")[:2] == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
    ]
    with pytest.raises(AssertionError):
        assert find_operation_by_description(operations, "sdfsdf")
    with pytest.raises(KeyError):
        assert find_operation_by_description(wrong_operations, "sdfsdf")


def test_find_categories():
    assert find_categories(operations, dict__) == {
        "Перевод организации": 40,
        "Перевод со счета на счет": 15,
        "Перевод с карты на карту": 19,
        "Открытие вклада": 10,
        "Перевод с карты на счет": 16,
    }
    with pytest.raises(KeyError):
        assert find_categories(wrong_operations, dict__)
    with pytest.raises(AssertionError):
        assert find_categories(wrong_operations, {})
