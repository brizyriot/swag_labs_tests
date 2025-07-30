import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_input = (By.CSS_SELECTOR, "#user-name")
    password_input = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_text = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Вход с логином {username}")
    def login(self, username, password):
        self.find(self.username_input).send_keys(username)
        self.find(self.password_input).send_keys(password)
        self.click(self.login_button)

    def get_error(self):
        return  self.find(self.error_text).text