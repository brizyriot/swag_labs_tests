import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.feature("Авторизация")
@allure.title("Авторизация с корректными данными")
@pytest.mark.parametrize("username, password",
                         [("standard_user", "secret_sauce"),
                          ("problem_user", "secret_sauce")])
def test_correct_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username,password)
    main_page = MainPage(driver)
    assert "Products" == main_page.get_main_title()


@allure.feature("Авторизация")
@allure.title("Авторизация с некорректными данными")
@pytest.mark.parametrize("username, password",
                         [("standard_user", "pass"),
                          ("user", "secret_sauce")])
def test_incorrect_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username,password)
    assert "Epic sadface" in login_page.get_error()