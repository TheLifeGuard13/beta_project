from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "operations.json")

ROOT_PATH_TEST = Path(__file__).parent
DATA_PATH_TEST = ROOT_PATH_TEST.joinpath("tests", "test_json.json")
