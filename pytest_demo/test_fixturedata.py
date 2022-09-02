import pytest
from pytest_demo.BaseClass import BaseClass
@pytest.mark.usefixtures('dataLoad')


class Test2(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.get_logger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
