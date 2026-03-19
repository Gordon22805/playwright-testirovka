from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_opened()


def test_invalid_login(page):
    login = LoginPage(page)

    login.open()
    login.login("wrong_user", "wrong_pass")

    assert "Epic sadface" in login.get_error_text()