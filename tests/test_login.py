import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username,password)
    main_page = MainPage(driver)
    assert "Products" == main_page.get_main_title()