import pytest

def test_addition():
    a = 5+10
    assert a==15

@pytest.mark.great
def test_greater_equal():
   num = 100
   print(num)
   assert num >= 100

@pytest.mark.skip
def test_subs():
   num = 100- 50
   print(num)
   assert num == 50

@pytest.mark.xfail
def test_div():
   num = 100//50
   print(num)
   assert num == 3

## the fixture will called befor test execution
@pytest.fixture
def setup():
   print('Hello I am a fixture!!')

## for calling a ficture before test execution we need to pass the fixture name to the test_step
def test_fixture_called(setup):
   print('Fixture is called.')