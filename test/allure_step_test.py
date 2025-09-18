import allure


@allure.step
def step_function_with_args(Розовые_розы, Светке_Соколовой):
    pass


@allure.step("Step with param '{param}'")
def step_with_placeholder(param):
    pass


@allure.step("Прокатило?")
def step_function_with_title():
    pass

@allure.epic("Allure TestOps")
def test_step():
    with allure.step("Проверка на цветы"):
        step_with_placeholder("Розы")
        with allure.step("Цвет"):
            step_function_with_args("Розовые", "Розы")
    step_function_with_title()
