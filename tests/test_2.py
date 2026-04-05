def test_demo1(): #обязательное наличие test
    assert 'meow' == 'meow'
import pytest


def test_demo2(before_after):
    assert 1 == 1

@pytest.fixture
def before_after():
    print ('before_test')
    yield
    print ('\nafter_test')