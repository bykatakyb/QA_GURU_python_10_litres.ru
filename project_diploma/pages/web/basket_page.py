import allure
from selene import browser, have, be


class BasketPage:
    def open(self):
        with allure.step("Перейти в корзину"):
            browser.open('my-books/cart/')
        return self

    def check_promo_inside_basket(self):
        with allure.step("Проверить что в корзине есть рекламное предложение"):
            browser.element('.FourArtGift_title___OYeB').should(
                have.text('Четвёртая книга в подарок'))
        return self

    def check_that_basket_is_empty(self):
        with allure.step("Проверить что корзина пуста"):
            browser.element('.EmptyState_empty__title__dZ7MW').should(have.text('Корзина пуста'))
        return self

    def check_added_product_inside_basket(self, product):
        with allure.step("Проверить наличие добавленного продукта в корзине"):
            browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(product.title))
            browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(product.writer))
            browser.element('[data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(product.price))
        return self

    def delete_product_from_basket(self):
        with allure.step("Удалить продукт из корзины"):
            browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
            browser.element('.Modal_controls__9uGUr > .Button_button_primary__k65Je').should(be.visible).click()
        return self

    def delete_product_from_basket_and_replace_it_to_favorite(self):
        with allure.step("Удалить продукт из корзины с переносом в отложенные"):
            browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
            browser.element('.Modal_layout__pyhtx > .Button_button_secondary__Apqdn').should(be.visible).click()
        return self


basket_page = BasketPage()
