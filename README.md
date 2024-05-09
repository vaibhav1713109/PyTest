## ***################ PyTest ################***

### **Key Concepts:**
- **Test discovery:** Pytest automatically discovers test functions named test_* or ending in _test within Python modules or directories.  
- **Fixtures:** Reusable code blocks that provide setup and teardown operations for tests, helping to isolate tests and reduce redundancy.  
- **Markers:** Metadata tags associated with tests to control their execution based on specific conditions or plugins.   
- **Command-line usage:** Pytest is invoked from the command line with various options to run, select, and configure tests.  

***################ Essential Commands ################***  
[Example file1](./PyTestDemos/test_demo1.py)
```
#define test >> start a function with name "test_"
def test_addition():
    a = 5+10
    assert 15 == a
```

**1. Running Tests:**  
- **pytest:** Runs all discovered tests in the current directory and its subdirectories.  
`test_demo1.py ..                                                                                       [100%]`  
- **pytest <filename.py> or pytest <directory>:** Runs tests from a specific file or directory.  
    - pytest test_demo1.py  
`test_demo1.py ..                                                                                       [100%]`  
- **pytest -k "keyword":** Runs tests containing the specified keyword in their name or docstring.  
    ```
    def test_addition():
        a = 5+10
        assert 15 == a
    ```
    - pytest -k "add" ## runs tests with "add" in their name or docstring.  
- **pytest -m "marker":** Runs tests marked with the given marker.
    ```
    import pytest
    @pytest.mark.great
    def test_greater_equal():
    num = 100
    assert num >= 100
    ```
    - pytest -m "great" ## runs tests marked with "great."
- **Skip Marker:** With Marker name skip we can skip the test.
    ```
    import pytest
    @pytest.mark.skip
    def test_subs():
    num = 100- 50
    assert num == 50
    ```
    - pytest test_demo1.py ## runs all tests and skip that have skip marker  
    `test_demo1.py ..s                                                                  [100%]`  

- **Xfail Marker:** With Marker name xfail it will run the test but not shows the PASSED or FAILED
    ```
    import pytest
    @pytest.mark.xfail
    def test_div():
    num = 100//50
    print(num)
    assert num == 2
    ```
    - pytest test_demo1.py ## runs all tests with Xfail  
    ```
    test_demo1.py::test_addition PASSED
    test_demo1.py::test_greater_equal 100
    PASSED
    test_demo1.py::test_subs SKIPPED (unconditional skip)
    test_demo1.py::test_div 2
    XFAIL

    ================================================= 2 passed, 1 skipped, 1 xfailed in 0.04s =================================================
    ```

**2. Fixtures:**  The fixture will called befor test executions and after the test execution   
[Fixture Example](./PyTestDemos/pytest_fixture.py)
```
    import pytest
    ## the fixture will called befor test execution
    @pytest.fixture
    def setup():
        print('Hello I am a fixture!! and executed before test started')
        yield
        print("I will execute after test completion.")

    ## for calling a ficture before test execution we need to pass the fixture name to the test_step
    def test_fixture_called(setup):
        print('Fixture is called.')
```
    
- pytest pytest_fixture.py  
```
PyTestDemos/pytest_fixture.py::test_fixture_called Hello I am a fixture!! and executed before test started
Fixture is called.
PASSEDI will execute after test completion.


=============================================================================== 1 passed in 0.01s ================================================================================
```

**3. Conftest:**  The conftest.py will be used to define common fixture and method which will be used in the test_*.py files inside test working directory  
[conftest.py Example](./PyTestDemos/conftest.py) >> One greating fixture defined inside it   
[test_demo1.py Example with calling greating fixture](./PyTestDemos/test_demo1.py) >> Greating fixture called in test_demo1.py  
[pytest_fixture.py Example](./PyTestDemos/pytest_fixture.py) >> Greating fixture called in pytest_fixture.py  
```
@pytest.fixture
def Greating():
   print('Hello I am a fixture!! and I will be executed before test started')
   yield
   print("I will execute after test completion, Bye!!")
```
```
pytest PyTestDemos/ -v -s

PyTestDemos/test_demo1.py::test_addition Hello I am a fixture!! and I will be executed before test started
PASSEDI will execute after test completion, Bye!!

PyTestDemos/test_demo1.py::test_greater_equal 100 PASSED
PyTestDemos/test_demo1.py::test_subs SKIPPED (unconditional skip)
PyTestDemos/test_demo1.py::test_div Hello I am a fixture!! and I will be executed before test started
2 XFAIL 
I will execute after test completion, Bye!!

PyTestDemos/test_pytest_fixture.py::test_fixture_called Hello I am a fixture!! and executed before test started Fixture is called. PASSED 
I will execute after test completion.

PyTestDemos/test_pytest_fixture.py::test_fixture_called1 Hello I am a fixture!! and I will be executed before test started
Greating fixture is called.
PASSED
I will execute after test completion, Bye!!


================================================= 4 passed, 1 skipped, 1 xfailed in 0.04s ==================================================
```

**4. Fixture Scope:**  The fixture have function, class, module and Session level scops.  

[fixture on multiple Method Example](./PyTestDemos/test_fixture_in_multiple_method.py)   
```
PyTestDemos/test_fixture_in_multiple_method.py::TestExample::test_fixture_called Hello I am a fixture!! and I will be executed before test started
test_fixture_called : Greating fixture is called.
PASSEDI will execute after test completion, Bye!!

PyTestDemos/test_fixture_in_multiple_method.py::TestExample::test_fixture_called1 Hello I am a fixture!! and I will be executed before test started
test_fixture_called1 : Greating fixture is called.
PASSEDI will execute after test completion, Bye!!

PyTestDemos/test_fixture_in_multiple_method.py::TestExample::test_fixture_called2 Hello I am a fixture!! and I will be executed before test started
test_fixture_called2 : Greating fixture is called.
PASSEDI will execute after test completion, Bye!!

PyTestDemos/test_fixture_in_multiple_method.py::TestExample::test_fixture_called3 Hello I am a fixture!! and I will be executed before test started
test_fixture_called3 : Greating fixture is called.
PASSEDI will execute after test completion, Bye!!


============================================================ 4 passed in 0.02s =============================================================
```
[Class level fixture](./PyTestDemos/test_fixture_class_scope.py)   
```
@pytest.fixture(scope='class')
def Greating2():
   print('Hi I am another fixture!! and I will be executed when a instance of class is executed')
   yield
   print("I will execute after the class scope finished, Bye!!")
```
```
PyTestDemos/test_fixture_class_scope.py::TestExample::test_class_fixture Hi I am another fixture!! and I will be executed when a instance of class is executed
test_class_fixture : Greating2 fixture is called.
PASSED
PyTestDemos/test_fixture_class_scope.py::TestExample::test_class_fixture1 test_class_fixture1 : Greating2 fixture is called.
PASSED
PyTestDemos/test_fixture_class_scope.py::TestExample::test_class_fixture2 test_class_fixture2 : Greating2 fixture is called.
PASSED
PyTestDemos/test_fixture_class_scope.py::TestExample::test_class_fixture3 test_class_fixture3 : Greating2 fixture is called.
PASSEDI will execute after the class scope finished, Bye!!


============================================================ 4 passed in 0.01s =============================================================
```

**5. Fixture Parametrize:**  We can pass parameters via fixture as well  
[conftest.py Example](./PyTestDemos/conftest.py) >> One greating fixture defined inside it    
[fixture params](./PyTestDemos/test_fixture_parameterize.py)  
```
@pytest.fixture(params=['CHrome','FireFox'])
def fixture_pram(request):
   return request.param

def test_callFixture_pram(fixture_pram):
    print(fixture_pram)
``` 

## ***################ Looging ################***  
```
Logging allows you to track events that happen during the execution of a program. It's a crucial tool for debugging, monitoring, and analyzing the behavior of your application.
```
[Logging Example](./LoggingEx/test_logging.py)  
[Logging Example](./LoggingEx/logger_method.py)  