import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo 1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo 2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo 3 method")

    def test_fixtureDemo4(self):
        print("i will execute steps in fixtureDemo 4 method")
