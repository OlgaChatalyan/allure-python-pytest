import allure
import pytest
from func import *

#@allure.id("2251")
@allure.title("Восстановление пароля")
#@allure.label("owner", "Alex")
@allure.epic("Aвторизация")
@allure.feature("Авторизация по email")
@allure.story("Восстановление пароля")
def test_pass_reset():
    with allure.step("Открыть главную страницу сайта"):
        pass
    with allure.step("Нажать кнопку Забыли пароль?"):
        pass
    with allure.step("Ввести email: ivanov.test@example.com"):
        pass
    with allure.step("Проверить почту: ivanov.test@example.com"):
        with allure.step("Expected Result"):
            with allure.step("Пришло письмо для восстановления пароля"):
                pass
            with allure.step("В письме есть ссылка для восстановления пароля"):
                pass
    with allure.step("Перейти по ссылке из письма"):
        with allure.step("Expected Result"):
            with allure.step("Открылась форма восстановления пароля"):
                pass
    with allure.step("Ввести новый пароль: NewTest12345!"):
        lucky_step()
        pass
    with allure.step("Подтвердить новый пароль: NewTest12345!"):
        lucky_step()
        pass
    with allure.step("Нажать кнопку Сохранить"):
        with allure.step("Expected Result"):
            with allure.step("Появляется сообщение Пароль изменен"):
                lucky_step()
                pass
    with allure.step("Авторизоваться с новым паролем"):
        with allure.step("Expected Result"):
            with allure.step("Авторизация успешна"):
                lucky_step()
                pass

#@allure.id("2301")
@allure.title("Логин с несуществующим email")
#@allure.label("owner", "Alex")
@allure.epic("Aвторизация")
@allure.feature("Авторизация по email")
@allure.story("Неуспешная авторизация")
def test_auth_error():
    with allure.step("Открыть главную страницу сайта"):
        pass
    with allure.step("Ввести email: test.ivanov@example.com"):
        pass
    with allure.step("Ввести пароль: Test12345!"):
        pass
    with allure.step("Нажать кнопку Войти"):
        with allure.step("Expected Result"):
            with allure.step("Ошибка: Пользователь не найден"):
                lucky_step()
                pass

#@allure.id("2324")
@allure.title("Отображение результатов поиска с корректной сортировкой")
#@allure.label("owner", "Alex")
@allure.epic("Поиск по каталогу")
@allure.feature("Поиск товаров")
@allure.story("Основной поиск")
def test_main_search_with_sort():
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("В поле поиска ввести Розовый пони"):
        pass
    with allure.step("Нажать Поиск"):
        with allure.step("Expected Result"):
            with allure.step("В результатах поиска есть Розовый пони S"):
                pass
            with allure.step("В результатах поиска есть Розовый пони M"):
                pass
            with allure.step("В результатах поиска есть Розовый пони L"):
                pass
            with allure.step("В результатах поиска есть Розовый пони XL"):
                lucky_step()
                pass
    with allure.step("Нажать Сортировка"):
        with allure.step("Expected Result"):
            with allure.step("Открылся выпадающий список с вариантами сортировки:"):
                lucky_step()
                pass
            with allure.step("По алфавиту (прямой)"):
                lucky_step()
                pass
            with allure.step("По алфавиту (обратный)"):
                lucky_step()
                pass
            with allure.step("По цене (дешевле - дороже)"):
                lucky_step()
                pass
            with allure.step("По цене (дороже - дешевле)"):
                lucky_step()
                pass
    with allure.step("Нажать поочередно на все варианты сортировки"):
        with allure.step("Expected Result"):
            with allure.step("Результаты поиска сортируются сразу при выборе нужного варианта сортировки"):
                lucky_step()
                pass
            with allure.step("Сортировка отрабатывается корректно, согласно выбранному варианту"):
                lucky_step()
                pass

#@allure.id("2322")
@allure.title("Поиск отсутствующего товара")
#@allure.label("owner", "Alex")
@allure.epic("Поиск по каталогу")
@allure.feature("Поиск товаров")
@allure.story("Основной поиск")
def test_search_missing_item():
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("В поле поиска ввести Розовый пони"):
        pass
    with allure.step("Нажать Поиск"):
        with allure.step("Expected Result"):
            with allure.step("В результатах поиска есть Розовый пони"):
                lucky_step()
                pass

#@allure.id("2323")
@allure.title("Поиск по артикулу")
#@allure.label("owner", "Alex")
@allure.epic("Поиск по каталогу")
@allure.feature("Поиск товаров")
@allure.story("Основной поиск")
def test_article_search():
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("В поле поиска ввести РП-012345"):
        pass
    with allure.step("Нажать Поиск"):
        with allure.step("Expected Result"):
            with allure.step("В результатах поиска есть Розовый пони"):
                lucky_step()
                pass

#@allure.id("2318")
@allure.title("Поиск по названию товара")
#@allure.label("owner", "Alex")
@allure.epic("Поиск по каталогу")
@allure.feature("Поиск товаров")
@allure.story("Основной поиск")
def test_name_search():
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("В поле поиска ввести Розовый пони"):
        pass
    with allure.step("Нажать Поиск"):
        with allure.step("Expected Result"):
            with allure.step("В результатах поиска есть Розовый пони"):
                lucky_step()
                pass

#@allure.id("2319")
@allure.title("Поиск по части названия товара")
#@allure.label("owner", "Alex")
@allure.epic("Поиск по каталогу")
@allure.feature("Поиск товаров")
@allure.story("Основной поиск")
def test_part_name_search():
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("В поле поиска ввести Розовый"):
        pass
    with allure.step("Нажать Поиск"):
        with allure.step("Expected Result"):
            with allure.step("В результатах поиска есть Розовый пони"):
                lucky_step()
                pass

#@allure.id("2253")
@allure.title("Верность расчета общей суммы прошлых заказов")
#@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Просмотр и редактирование профиля")
@allure.story("История заказов")
def test_order_history():
    with allure.step("Перейти в личный кабинет"):
        pass
    with allure.step("Нажать История заказов"):
        with allure.step("Expected Result"):
            with allure.step("Отображается таблица с историей заказов"):
                pass
            with allure.step("Есть столбец со стоимостью заказов"):
                pass
            with allure.step("Под таблицей корректно отображается информация об общей сумме всех заказов в виде числа"):
                lucky_step()
                pass
    with allure.step("Сложить стоимости всех заказов"):
        lucky_step()
        pass
    with allure.step("Сравнить полученную сумму стоимости заказов и сравнить с суммой, отображаемой в личном кабинете"):
        lucky_step()
        pass

#@allure.id("2298")
@allure.title("Отображение избранных товаров")
#@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Список товаров")
@allure.story("Избранное")
def test_show_favorite_items():
    with allure.step("Перейти в избранное"):
        pass
    with allure.step("Убедиться что в избранном есть товары"):
        lucky_step()
        pass

#@allure.id("2304")
@allure.title("Отображение товаров в корзине")
#@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Список товаров")
@allure.story("Корзина")
def test_items_in_card():
    with allure.step("Перейти в корзину"):
        pass
    with allure.step("Убедиться что в корзине есть товары"):
        lucky_step()
        pass
