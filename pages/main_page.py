from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    main_title = (By.CSS_SELECTOR, "[data-test='title']")

    def get_main_title(self):
        return self.find(self.main_title).text