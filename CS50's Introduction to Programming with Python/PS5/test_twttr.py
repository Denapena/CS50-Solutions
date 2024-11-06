from twttr import shorten

def test_short():
    assert shorten("abrakadabrabra") == "brkdbrbr"
    assert shorten("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == ""

def test_long():
    assert shorten("brkmrkstrk") == "brkmrkstrk"
    assert shorten("avion") == "vn"