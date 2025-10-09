import allure

@allure.title("Демонстрационный ручной тест")
@allure.story("Story")
@allure.feature("Feature")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("example")
@allure.label("owner", "mlankin")
@allure.manual(True)
def test_demo_manual():
    with allure.step("Демонстрационный шаг"):
        pass
