# Any pytest file should start with test_ or ebd with _test
# pytest method names should start with test
# any code should be wrapped in method
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail it will run but not showing test case
# fixture are used as setup and tear down methods for test case- conftest file to generalize fixture and make it ->
# --> available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because test case not match"


def test_firstCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Test case not matched"