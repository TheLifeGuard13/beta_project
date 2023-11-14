import pytest

from config import DATA_PATH_TEST, DATA_PATH_TEST2
from src.utils import check_currency, load_file, pick_one_operation


@pytest.fixture
def list_operations() -> list[dict]:
    return load_file(DATA_PATH_TEST)


def test_load_file(list_operations):
    assert load_file(DATA_PATH_TEST) == list_operations
    assert load_file(DATA_PATH_TEST2) == []
    assert load_file("./src/test_json.json") == []


def test_pick_one_operation():
    test_list = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}, {"f": 6}, {"g": 7}]
    test_pick_one = pick_one_operation(test_list)
    test_pick_two = pick_one_operation(test_list)
    test_pick_three = pick_one_operation(test_list)
    assert test_pick_one != test_pick_two or test_pick_two != test_pick_three


def test_check_currency(list_operations):
    assert check_currency(list_operations[0]) == 31957.58
    with pytest.raises(TypeError):
        assert check_currency(list_operations[1])
    with pytest.raises(TypeError):
        assert check_currency(list_operations[2])
    with pytest.raises(KeyError):
        assert check_currency(list_operations[3])
    with pytest.raises(ValueError):
        assert check_currency(list_operations[4])
    with pytest.raises(Exception):
        assert check_currency(list_operations[5])
