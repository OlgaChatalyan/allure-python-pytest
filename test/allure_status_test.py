import pytest
import allure
from allure import attachment_type
from allure_commons.types import Severity

@allure.epic("Allure TestOps")
def test_passed():
    pass

@allure.epic("Allure TestOps")
def test_failed():
    assert False, "Some fail reason"

@allure.epic("Allure TestOps")
def test_broken():
    var = 1 / 0
    assert var


@pytest.mark.skip(reason="Some skip reason")
@allure.epic("Allure TestOps")
def test_skipped():
    pass


@pytest.mark.xfail(reason="Some xfail reason")
@allure.epic("Allure TestOps")
def test_xfail():
    assert False, "Assertion failed"


@pytest.mark.xfail(reason="Test doesn't fail")
@allure.epic("Allure TestOps")
def test_xpass():
    pass
