import allure
import pyperclip
from selene import browser, be, have
from selenium.webdriver import Keys


class HomePage:
    def open(self):
        with allure.step("Открыть главную страницу"):
            browser.open("/")
            return self

    def do_authorization(self, customer):
        with allure.step("Авторизоваться"):
            browser.element('[href="/pages/login/"]').should(be.visible).click()
            browser.element('[name="email"]').should(be.visible).type(customer.email)
            browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
            browser.element('[name="pwd"]').should(be.visible).type(customer.password)
            browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        return self

    def check_authorization_status_positive(self, customer):
        with allure.step("Проверить авторизацию (позитивный кейс)"):
            browser.element('.ProfileButton_profileButton__Agdcv').should(be.visible).click()
            browser.open("pages/personal_cabinet_about_me/")
            browser.element('span[class="user_header__name"]').should(have.text(customer.name))
        return self

    def check_authorization_status_negative(self):
        with allure.step("Проверить авторизацию (негативный кейс)"):
            browser.element('.ControlInput_input__error__0DtKl').should(
                have.text('Неверное сочетание логина и пароля'))
        return self

    def search_product_using_title(self, product):
        with allure.step("Выполенить поиск продукта по названию"):
            pyperclip.copy(product.title)

            browser.element('[data-testid="search__input"]').click().press(Keys.CONTROL + 'v')
            browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    def check_searched_product_title_in_search_results(self, product):
        with allure.step("Проверить наличие искомого (по названию) продукта в результатах поиска"):
            browser.element('[data-testid="art__title"]').should(have.text(f'{product.title}'))
        return self

    def search_product_using_writer(self, product):
        with allure.step("Выполенить поиск продукта по писателю"):
            pyperclip.copy(product.writer)

            browser.element('[data-testid="search__input"]').click().press(Keys.CONTROL + 'v')
            browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    def check_searched_product_writer_in_search_results(self, product):
        with allure.step("Проверить наличие искомого (по писателю) продукта в результатах поиска"):
            browser.element('[data-testid="art__authorName"]').should(have.text(f'{product.writer}'))
        return self


home_page = HomePage()
