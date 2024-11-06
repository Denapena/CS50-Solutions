from fuel import gauge
from fuel import convert
import pytest

def test_gauge1():
    assert gauge(1) == "E"

def test_gauge2():
    assert gauge(75) == "75%"

def test_convert1():
    assert convert("3/4") == 75

def test_convert2():
    assert convert("1/1") == 100

def test_convert3():
    assert convert("1/100") == 1

def test_convert4():
    with pytest.raises(ValueError):
        convert("dog")
