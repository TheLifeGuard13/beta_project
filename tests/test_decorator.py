import pytest

from src.decorator import my_function


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, 2),
        ("1", "2", "12"),
        (True, True, 2),
        (None, None, None),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
        (1, None, None),
        ("1", 1, None),
    ],
)
def test_my_function(x, y, expected):
    assert my_function(x, y) == expected
