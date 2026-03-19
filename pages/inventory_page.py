class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = ".title"
        self.add_to_cart_btn = ".inventory_item button"
        self.cart_link = ".shopping_cart_link"

    def is_opened(self):
        return self.page.locator(self.title).text_content() == "Products"

    def add_first_item_to_cart(self):
        self.page.locator(self.add_to_cart_btn).first.click()

    def go_to_cart(self):
        self.page.click(self.cart_link)