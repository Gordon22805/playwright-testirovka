class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"
        self.checkout_button = "#checkout"

    def get_items_count(self):
        return self.page.locator(self.cart_items).count()

    def checkout(self):
        self.page.click(self.checkout_button)