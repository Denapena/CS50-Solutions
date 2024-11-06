from bank import value
import pytest

def test_bank_str():
    assert value("hhhhhhhhhhhhhhhh") == "$20"

def test_bank_int():
    with pytest.raises(AttributeError):
        value(50)


def test_bank_float():
    with pytest.raises(AttributeError):
        value(True)