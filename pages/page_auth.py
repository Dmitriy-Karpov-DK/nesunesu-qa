import allure

from locators import LocatorMainPages
from pages.page_main import MainPage


class AuthPage(MainPage):

    @allure.step('Клик по кнопке Далее')
    def click_on_next(self):
        self.click_method(LocatorMainPages.BUTTON_NEXT_POP_UP_WINDOW_AUTH)

    @allure.step('Вводим номер телефона')
    def set_phone(self, phone):
        self.send_keys_method(LocatorMainPages.FIELD_INPUT_PHONE_POP_UP_WINDOW_AUTH, phone)

    @allure.step('Клик по чек-боксу ознакомления с пользовательским соглашением'
                 ' и согласия на обработку персональных данных')
    def click_on_checkbox(self):
        self.click_method(LocatorMainPages.BUTTON_CHECKBOX_POP_UP_WINDOW_AUTH)

    @allure.step('Вводим 1 цифру кода')
    def set_confirmation_code1(self, code):
        self.send_keys_method(LocatorMainPages.FIELD_INPUT_CONFIRMATION_CODE_1, code)

    @allure.step('Вводим 2 цифру кода')
    def set_confirmation_code2(self, code):
        self.send_keys_method(LocatorMainPages.FIELD_INPUT_CONFIRMATION_CODE_2, code)

    @allure.step('Вводим 3 цифру кода')
    def set_confirmation_code3(self, code):
        self.send_keys_method(LocatorMainPages.FIELD_INPUT_CONFIRMATION_CODE_3, code)

    @allure.step('Вводим 4 цифру кода')
    def set_confirmation_code4(self, code):
        self.send_keys_method(LocatorMainPages.FIELD_INPUT_CONFIRMATION_CODE_4, code)
