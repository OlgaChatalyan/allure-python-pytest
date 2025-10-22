import allure
import pytest


@allure.id("2616")
@allure.tag("Edu_tests")
@allure.title("Проверка авторизации с разными наборами логина/пароля")
@allure.label("owner", "Ольга Ч")
@allure.epic("Регистрация и авторизация")
@allure.feature("Авторизация")
@allure.story("Регистрация по email и пароль")
def test_method():
    allure.dynamic.label("severity", "Высокий");
    with allure.step("Открыть страницу логина"):
        pass
    with allure.step("Ввести в поле Username тестовый логин"):
        pass
    with allure.step("Ввести в поле Password тестовый пароль"):
        pass
    with allure.step("Нажать Login"):
        pass
    sharedStep306()


@allure.step("Сайт 36.6 поисковая строка")
def sharedStep306():
    with allure.step("Зайти на сайт https://366.ru/"):
        pass
    with allure.step("Нати поисковую строку"):
        with allure.step("Attachment [49]"):
            pass

