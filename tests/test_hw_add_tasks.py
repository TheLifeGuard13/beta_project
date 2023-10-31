import pytest

from src.hw_add_tasks import count_files_from_path, get_format_string, get_nums_multiple


@pytest.mark.parametrize(
    "path, recursive, expected",
    [
        ("/home/vlad/PycharmProjects/beta_project/", False, {"files": 4, "folders": 4}),
        ("/home/vlad/PycharmProjects/beta_project/", True, {"files": 875, "folders": 125}),
    ],
)
def test_count_files_from_path(path, recursive, expected):
    assert count_files_from_path(path, recursive) == expected


@pytest.mark.parametrize(
    "words_list, expected",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        (["", "madam", "racecar", "noon", "level", ""], ["", "madam", "racecar", "noon", "level", ""]),
        ([], []),
    ],
)
def test_get_format_string(words_list, expected):
    assert get_format_string(words_list) == expected


@pytest.mark.parametrize(
    "int_list, expected", [([2, 3, 5, 7, 11], 77), ([-5, -7, -9, -13], 117), ([1, 2], 2), ([4], 0)]
)
def test_get_nums_multiple(int_list, expected):
    assert get_nums_multiple(int_list) == expected
