import pytest
## the fixture will called befor test execution
@pytest.fixture
def setup():
   print('Hello I am a fixture!!')

## for calling a ficture before test execution we need to pass the fixture name to the test_step
def test_fixture_called(setup):
   print('Fixture is called.')