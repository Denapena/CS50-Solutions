from plates import is_valid


def test_1():
    assert is_valid("A1BC23") == False

def test_2():
    assert is_valid("AABC23453") == False


def test_3():
    assert is_valid("AAASD?") == False

def test_4():
    assert is_valid("AABC23") == True

def test_5():
    assert is_valid("AAB023") == False