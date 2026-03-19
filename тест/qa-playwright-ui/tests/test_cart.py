from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_opened()

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert cart.get_items_count() == 1