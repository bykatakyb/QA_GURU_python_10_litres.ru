import allure
from selene import browser, have


class BasketPage:
    def open(self):
        with allure.step("Перейти в корзину"):
            browser.open('my-books/cart/')
        return self

    def check_that_basket_is_empty(self):
        with allure.step("Проверить что корзина пуста"):
            browser.element('.EmptyState_empty__title__dZ7MW').should(have.text('Корзина пуста'))
        return self


basket_page = BasketPage()
