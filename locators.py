from selenium.webdriver.common.by import By


class LocatorMainPages:

    BUTTON_LOGIN = (By.CSS_SELECTOR, "a.text-sm[href='/#auth']")
    BUTTON_NEXT_POP_UP_WINDOW_AUTH = (By.CSS_SELECTOR, "div.flex button[type='submit']")
    FIELD_INPUT_PHONE_POP_UP_WINDOW_AUTH = (By.CSS_SELECTOR, "div.react-tel-input input")
    BUTTON_CHECKBOX_POP_UP_WINDOW_AUTH = (By.CSS_SELECTOR, "label.flex input.hm-checkbox")
    FIELD_INPUT_CONFIRMATION_CODE_1 = (By.CSS_SELECTOR, "input[aria-label='pin code 1 of 4']")
    FIELD_INPUT_CONFIRMATION_CODE_2 = (By.CSS_SELECTOR, "input[aria-label='pin code 2 of 4']")
    FIELD_INPUT_CONFIRMATION_CODE_3 = (By.CSS_SELECTOR, "input[aria-label='pin code 3 of 4']")
    FIELD_INPUT_CONFIRMATION_CODE_4 = (By.CSS_SELECTOR, "input[aria-label='pin code 4 of 4']")
    BUTTON_PROFILE = (By.CSS_SELECTOR, "div.items-center a[href='/profile']")
