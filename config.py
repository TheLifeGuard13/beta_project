from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "operations.json")

ROOT_PATH_TEST = Path(__file__).parent
DATA_PATH_TEST = ROOT_PATH_TEST.joinpath("tests", "tests_data", "test_json.json")

ROOT_PATH_TEST2 = Path(__file__).parent
DATA_PATH_TEST2 = ROOT_PATH_TEST2.joinpath("tests", "tests_data", "test2_json.json")

ROOT_PATH_CSV = Path(__file__).parent
DATA_PATH_CSV = ROOT_PATH_CSV.joinpath("data", "transactions.csv")

ROOT_PATH_XLS = Path(__file__).parent
DATA_PATH_XLS = ROOT_PATH_XLS.joinpath("data", "transactions_excel.xlsx")

ROOT_PATH_TEST3 = Path(__file__).parent
DATA_PATH_TEST3 = ROOT_PATH_TEST3.joinpath("tests", "tests_data", "test_json3.json")
