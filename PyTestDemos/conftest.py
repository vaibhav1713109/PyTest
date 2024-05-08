"""
With the help of conftest.py file we can call the fixture and methods defined in the conftest.py 
in all test_*.py files
"""

import pytest
## the fixture will called befor test execution
@pytest.fixture
def Greating():
   print('Hello I am a fixture!! and I will be executed before test started')
   yield
   print("I will execute after test completion, Bye!!")


@pytest.fixture(scope='class')
def Greating2():
   print('Hi I am another fixture!! and I will be executed when a instance of class is executed')
   yield
   print("I will execute after the class scope finished, Bye!!")



@pytest.fixture(params=['CHrome','FireFox'])
def fixture_pram(request):
   return request.param