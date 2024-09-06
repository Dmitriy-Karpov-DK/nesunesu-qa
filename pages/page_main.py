import allure

from locators import LocatorMainPages
from pages.base_page_nesunesu import BasePagesNN


class MainPage(BasePagesNN):

    @allure.step('Клик по кнопке Войти')
    def click_on_login(self):
        self.click_method(LocatorMainPages.BUTTON_LOGIN)
