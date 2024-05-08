## ***################ PyTest ################***

### **Key Concepts:**
- **Test discovery:** Pytest automatically discovers test functions named test_* or ending in _test within Python modules or directories.  
- **Fixtures:** Reusable code blocks that provide setup and teardown operations for tests, helping to isolate tests and reduce redundancy.  
- **Markers:** Metadata tags associated with tests to control their execution based on specific conditions or plugins.   
- **Command-line usage:** Pytest is invoked from the command line with various options to run, select, and configure tests.  

***################ Essential Commands ################***  
[Example file1](./Selenium_practice/test_demo1.py)
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

**2. Fixtures:**  The fixture will called befor test executions.   
[Fixture Example](./Selenium_practice/pytest_fixture.py)
```
    import pytest
    ## the fixture will called befor test execution
    @pytest.fixture
    def setup():
        print('Hello I am a fixture!!')
    ## for calling a ficture before test execution we need to pass the fixture name to the test_step
    def test_fixture_called(setup):
        print('Fixture is called.')
```
    
- pytest pytest_fixture.py 
```
PyTestDemos/pytest_fixture.py::test_fixture_called Hello I am a fixture!!
Fixture is called.
PASSED

================================================= 1 passed in 0.01s =================================================
```