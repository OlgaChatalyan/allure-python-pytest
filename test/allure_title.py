import allure
import pytest
from allure import attachment_type
from allure_commons.types import Severity


@allure.title("Some title for test")
@allure.epic("Allure TestOps")
def test_with_title():
    pass


@allure.title("Test title with param {param}")
@pytest.mark.parametrize("param", ["first", "second"])
@allure.epic("Allure TestOps")
def test_with_dynamic_title(param):
    pass


@allure.title("Fixture title")
@pytest.fixture()
def titled_fixture():
    pass

@allure.epic("Allure TestOps")
def test_with_titled_fixture(titled_fixture):
    pass
