from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "operations.json")

ROOT_PATH_TEST = Path(__file__).parent
DATA_PATH_TEST = ROOT_PATH_TEST.joinpath("tests", "test_json.json")

ROOT_PATH_TEST2 = Path(__file__).parent
DATA_PATH_TEST2 = ROOT_PATH_TEST2.joinpath("tests", "test2_json.json")