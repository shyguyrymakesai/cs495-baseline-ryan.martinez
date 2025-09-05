import pytest
from utils import lower_concat


def test_lower_concat_hw():
    assert lower_concat(["Hello", "WORLD"]) == "helloworld"


def test_lower_concat_empty():
    assert lower_concat([]) == ""


def test_lower_concat_mixed():
    assert lower_concat(["PyThOn", "TeSt"]) == "pythontest"


test_lower_concat_empty()
test_lower_concat_hw()
test_lower_concat_mixed()
