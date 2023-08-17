import pytest
from BaseClass import BaseClassOne


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClassOne):
    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        log.info("information printed")
        log.info(dataLoad)
        log.info(dataLoad[2])


# def test_crossBrowser(cross_browser):
#     print(cross_browser[1])