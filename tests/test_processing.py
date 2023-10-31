import pytest

from src.processing import get_formatted_list, get_formatted_list_by_date, get_sorted_by_price


@pytest.fixture
def coll():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_get_formatted_list_by_status(coll):
    assert get_formatted_list(coll, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_get_formatted_list_by_date(coll):
    assert get_formatted_list_by_date(coll) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_get_formatted_list_by_date2(coll):
    assert get_formatted_list_by_date(coll, False) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def coll_two():
    return [
        {"name": "Apple", "price": 2.50, "category": "fruit", "quantity": 100},
        {"name": "Grape", "price": 10.30, "category": "fruit", "quantity": 10},
        {"name": "Banana", "price": 1.20, "category": "fruit", "quantity": 500},
        {"name": "Cucumber", "price": 6.80, "category": "vegetable", "quantity": 30},
        {"name": "Onion", "price": 0.75, "category": "vegetable", "quantity": 75},
    ]


def test_get_sorted_by_price_category(coll_two):
    assert get_sorted_by_price(coll_two, "fruit") == [
        {"name": "Banana", "price": 1.2, "category": "fruit", "quantity": 500},
        {"name": "Apple", "price": 2.5, "category": "fruit", "quantity": 100},
        {"name": "Grape", "price": 10.3, "category": "fruit", "quantity": 10},
    ]


def test_get_sorted_by_price(coll_two):
    assert get_sorted_by_price(coll_two) == [
        {"name": "Onion", "price": 0.75, "category": "vegetable", "quantity": 75},
        {"name": "Banana", "price": 1.2, "category": "fruit", "quantity": 500},
        {"name": "Apple", "price": 2.5, "category": "fruit", "quantity": 100},
        {"name": "Cucumber", "price": 6.8, "category": "vegetable", "quantity": 30},
        {"name": "Grape", "price": 10.3, "category": "fruit", "quantity": 10},
    ]
