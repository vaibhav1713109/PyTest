"""
Scenario 1: if there are multiple methods in which we have to use the fixture before the class start and
         after the class scope finished.
"""
import pytest

@pytest.mark.usefixtures('Greating2')
class TestExample:
    def test_class_fixture(self):
        print('test_class_fixture : Greating2 fixture is called.')

    def test_class_fixture1(self):
        print('test_class_fixture1 : Greating2 fixture is called.')

    def test_class_fixture2(self):
        print('test_class_fixture2 : Greating2 fixture is called.')

    def test_class_fixture3(self):
        print('test_class_fixture3 : Greating2 fixture is called.')