import allure
from selene import browser, have


class FavoritePage:
    def open(self):
        with allure.step("Перейти в отложенные"):
            browser.open('my-books/liked/')
        return self

    def check_that_favorite_is_empty(self):
        with allure.step("Проверить что в отложенных пусто"):
            browser.element('.ReadAndListenSlider_text__vmtu1').should(
                have.text('Здесь будет появляться все, что вы читаете и слушаете'))
        return self


favorite_page = FavoritePage()
