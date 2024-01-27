from twttr import shorten
import pytest

def test_lowercase():
    assert shorten('lowercase') == 'lwrcs'


def test_uppercase():
    assert shorten('UPPERCASE') == 'PPRCS'


def test_digits():
    # with pytest.raises(TypeError):
    assert shorten('1') == '1'


def test_punctuation():
    assert shorten(',..//,') == ',..//,'
