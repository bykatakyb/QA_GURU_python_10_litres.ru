import allure
from selene import browser, be


class ProductPage:
    def open(self, product):
        with allure.step("Перейти на страницу продукта"):
            browser.open(product.url)
        return self

    def add_product_to_basket(self):
        with allure.step("Добавить продукт в корзину"):
            browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
            browser.driver.refresh()
        return self


product_page = ProductPage()
