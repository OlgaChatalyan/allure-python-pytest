import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

@allure.tag('UI Tests')
@allure.severity(allure.severity_level.MAJOR)
@allure.label('layer', 'UI Tests')
@allure.feature('Google search')
@allure.title('Search for "Quokka images" in Google and take a screenshot')
def test_google_search_quokka_images(tmp_path):
    # Настройка Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Убрать, если нужен видимый браузер
    driver = webdriver.Chrome(options=chrome_options)

    try:
        with allure.step("Open google.com"):
            driver.get("https://www.google.com")
            time.sleep(1)  # Подождать подгрузку (лучше заменить на WebDriverWait)

        with allure.step('Accept cookies if present'):
            try:
                agree_button = driver.find_element(By.XPATH, "//div[text()='Accept all' or text()='Принять все']")
                agree_button.click()
                time.sleep(1)
            except:
                pass  # Нет окна с cookies — продолжаем

        with allure.step('Enter search query "Quokka images"'):
            search_input = driver.find_element(By.NAME, 'q')
            search_input.send_keys("Quokka images")
            search_input.send_keys(Keys.RETURN)
            time.sleep(2)

        with allure.step('Take screenshot of the search results'):
            screenshot_path = tmp_path / "quokka_search.png"
            driver.save_screenshot(str(screenshot_path))
            allure.attach.file(
                str(screenshot_path),
                name="Quokka Search Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    finally:
        driver.quit()
