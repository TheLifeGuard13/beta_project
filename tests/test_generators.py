import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.main import transactions


@pytest.fixture
def coll():
    return transactions


@pytest.mark.parametrize(
    "currency, expected", [("USD", [939719570, 142264268, 895315941]), ("RUB", [873106923, 594226727])]
)
def test_filter_by_currency(coll, currency, expected):
    usd_transactions = filter_by_currency(coll, currency)
    assert [i["id"] for i in list(usd_transactions)] == expected


def test_transaction_descriptions(coll):
    assert list(transaction_descriptions(coll)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999, 10002, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001", "0000 0000 0001 0002"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(number for number in card_number_generator(start, stop)) == expected
