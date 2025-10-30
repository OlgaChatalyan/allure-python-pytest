import allure


@allure.step
def step_function_with_args(Цвет, Цветы):
    pass


@allure.step("Дветы для Светки Соколовой '{param}'")
def step_with_placeholder(param):
    pass


@allure.step("Прокатило!")
def step_function_with_title():
    pass

@allure.epic("Allure TestOps")
@allure.label("tag", "Regression")
def test_step():
    with allure.step("Проверка на цветы"):
        step_with_placeholder("Розы")
        with allure.step("Цвет"):
            step_function_with_args("Розовые", "Розы")
    step_function_with_title()
