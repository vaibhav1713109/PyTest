"""
Scenario 1: if there are multiple methods in which we have to use the fixture but we don't pass that ficture to the function
        instead of that we can create a class for those method use fixture with below.
"""
import pytest

@pytest.mark.usefixtures('Greating')
class TestExample:
    def test_fixture_called(self):
        print('test_fixture_called : Greating fixture is called.')

    def test_fixture_called1(self):
        print('test_fixture_called1 : Greating fixture is called.')

    def test_fixture_called2(self):
        print('test_fixture_called2 : Greating fixture is called.')

    def test_fixture_called3(self):
        print('test_fixture_called3 : Greating fixture is called.')