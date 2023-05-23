import pytest


def testLogin():
    print("Login Successful")


def testLogoff():
    print("Logoff Successful")


@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 != 6
