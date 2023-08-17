# any pytest file should start  with test_ or end with _test
# pytest method should start with test
# pytest methods are treated as test cases
# to run pytest method (on testcase file path )<pytest >
# to run a particular file <pytest filename.py -k testcasename -v -s >
# -k for test case name or method name execution, -v for more info metadata, -s for logs in output
# you can run specififile with pytest <filename>
# to group test cases pytest -m <groupname> -v -s
# to skip test @pytest.mark.skip
# you can run but doesn't want to report in output with @pytest.mark.xfail
# fixtures are used for setup and teardown for testcases , conftest file to generalize fixture  and make available to all the testcases
# if you want to return some values from fixture, then even if u have declared fixture on class level still you need to pass fixture method name as arugument where u are calling fixture
# data driven and parameterization can be done with return statement with tuple format
# when you define fixture scope to class only , it will run once before class is initiated and at the end




import pytest


@pytest.mark.Sanity
@pytest.mark.xfail
def testfirstCrditCard():
    msg = "Hi"
    print("Hello")
    assert msg == "Hello", "does not match"


@pytest.mark.skip
def testSecond():
    print("second test executed")
