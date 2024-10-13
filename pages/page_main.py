import allure

from locators import LocatorMainPages
from pages.base_page_nesunesu import BasePagesNN


class MainPage(BasePagesNN):

    @allure.step('Клик по кнопке Войти')
    def click_on_login(self):
        self.click_method(LocatorMainPages.BUTTON_LOGIN)

    @allure.step('Клик по кнопке Профиль')
    def click_on_profile(self):
        self.click_method(LocatorMainPages.BUTTON_PROFILE)

    @allure.step('Клик по кнопке Соглашения об обработке перс.данных')
    def click_on_accept_pers_data(self):
        self.click_method(LocatorMainPages.BUTTON_ACCEPT_PERS_DATA)
