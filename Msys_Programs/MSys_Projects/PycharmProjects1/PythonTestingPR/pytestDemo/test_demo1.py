# Any pytest file should start with test_ or ebd with _test
# pytest method names should start with test
# any code should be wrapped in method
# @pytest.mark.xfail
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_firstCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])