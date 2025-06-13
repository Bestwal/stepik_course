import pytest


def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    a = 3
    b = 2
    assert a + b == 6

def test_not_succed():
    assert True

@pytest.mark.skip
def test_skipped():
    assert False