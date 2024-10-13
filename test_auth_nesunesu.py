import allure
import pytest

from constants import Constants
from pages.page_auth import AuthPage
from locators import LocatorMainPages


class TestAuth:

    @allure.title('Проверим авторизацию при валидных значениях')
    def test_auth_positive_values_successful(self, driver):
        test_page = AuthPage(driver)
        test_page.waite_invisible_element(LocatorMainPages.ELEMENT_HIDING_BUTTON_LOGIN)
        test_page.wait_clickable(LocatorMainPages.BUTTON_LOGIN)
        test_page.click_on_login()
        test_page.expectation(LocatorMainPages.FIELD_INPUT_PHONE_POP_UP_WINDOW_AUTH)
        test_page.set_phone(9000000000)
        test_page.click_on_checkbox()
        test_page.click_on_next()
        test_page.expectation(LocatorMainPages.FIELD_INPUT_CONFIRMATION_CODE_1)
        test_page.set_confirmation_code1(4)
        test_page.set_confirmation_code2(7)
        test_page.set_confirmation_code3(4)
        test_page.set_confirmation_code4(7)
        test_page.waite_invisible_element(LocatorMainPages.ELEMENT_HIDING_BUTTON_PROFILE)
        test_page.wait_clickable(LocatorMainPages.BUTTON_PROFILE)
        test_page.click_on_profile()
        test_page.expectation(LocatorMainPages.ELEMENT_HEAD_PROFILE_PAGE)
        assert test_page.get_url() == Constants.URL_PROFILE
