import pytest
import allure

from selenium import webdriver
from constants import Constants


@allure.step('Инициализируем браузер и после действий удаляем')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Constants.URL_BASE)
        yield driver
        driver.quit()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Constants.URL_BASE)
        yield driver
        driver.quit()
    else:
        pass
