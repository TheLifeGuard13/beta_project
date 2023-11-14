import datetime
import os.path

import pytest

from src.decorator import log


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, " func ok"),
        ("1", 1, ''' func error: <can only concatenate str (not "int") to str>. Inputs: ('1', 1), {}'''),
        (
            None,
            None,
            " func error: <unsupported operand type(s) for +: 'NoneType' and 'NoneType'>. Inputs: (None, None), {}",
        ),
    ],
)
def test_log(x, y, expected):
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def func(a, b):
        return a + b

    date_now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    func(x, y)

    with open(filename) as f:
        log_message = f.read().strip()

    expected_log = date_now + expected

    assert log_message == expected_log


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, " func ok"),
        ("1", 1, """ func error: <can only concatenate str (not "int") to str>. Inputs: ('1', 1), {}"""),
        (
            None,
            None,
            " func error: <unsupported operand type(s) for +: 'NoneType' and 'NoneType'>. Inputs: (None, None), {}",
        ),
    ],
)
def test_console_log(capsys, x, y, expected):
    @log()
    def func(a, b):
        return a + b

    date_now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    func(x, y)

    expected_log = date_now + expected

    log_message = capsys.readouterr().out.strip()

    assert log_message == expected_log
