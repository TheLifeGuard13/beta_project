from pathlib import Path

import pandas as pd
import pytest

from config import DATA_PATH_CSV, DATA_PATH_TEST2, DATA_PATH_TEST3, DATA_PATH_XLS
from src.converters import load_csv_file, load_json_file, load_xlsx_file

DATA_PATH_TEST4 = Path(__file__).parent.parent.joinpath("tests", "tests_data", "empty_file.csv")
DATA_PATH_TEST5 = Path(__file__).parent.parent.joinpath("tests", "tests_data", "file.csv")
DATA_PATH_TEST6 = Path(__file__).parent.parent.joinpath("tests", "tests_data", "test.txt")


def test_load_csv_file():
    assert load_csv_file(DATA_PATH_CSV).shape == (1000, 9)
    assert load_csv_file(DATA_PATH_TEST5).shape == (3, 1)
    with pytest.raises(FileNotFoundError):
        assert load_csv_file("./src/test_json.json")
    with pytest.raises(pd.errors.EmptyDataError):
        assert load_csv_file(DATA_PATH_TEST4)
    with pytest.raises(ValueError):
        assert load_csv_file(DATA_PATH_TEST6)


def test_load_xlsx_file():
    assert load_xlsx_file(DATA_PATH_XLS).shape == (1000, 9)
    with pytest.raises(FileNotFoundError):
        assert load_xlsx_file("./src/test_json.json")
    with pytest.raises(ValueError):
        assert load_xlsx_file(DATA_PATH_TEST6)


def test_load_json_file():
    assert load_json_file(DATA_PATH_TEST3) == [{"id": 441945883, "name": "Перев"}]
    assert load_json_file(DATA_PATH_TEST2) == []
    assert load_json_file("./src/test_json.json") == []
