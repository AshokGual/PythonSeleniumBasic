import pytest

from BaseClass import BaseClassOne


@pytest.mark.usefixtures("testsetup")
class TestExample(BaseClassOne):

    def test_execute1(self):
        log = self.getlogger()
        log.info("log executed/................")
        print("test example1")

    def test_execute2(self):
        print("test example2")

    def test_execute3(self):
        print("test example3")

    def test_execute4(self):
        print("test example4")


