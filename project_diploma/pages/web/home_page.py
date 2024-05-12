import allure
from selene import browser, be, have


class HomePage:
    def open(self):
        with allure.step("Открытие главной страницы"):
            browser.open("/")
            return self

    def do_authorization(self, customer):
        with allure.step("Авторизация"):
            browser.element('[href="/pages/login/"]').should(be.visible).click()
            browser.element('[name="email"]').should(be.visible).type(customer.email)
            browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
            browser.element('[name="pwd"]').should(be.visible).type(customer.password)
            browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        return self

    def check_authorization_status_positive(self, customer):
        with allure.step("Проверка авторизации (позитивный кейс)"):
            browser.element('.ProfileButton_profileButton__Agdcv').should(be.visible).click()
            browser.open("pages/personal_cabinet_about_me/")
            browser.element('span[class="user_header__name"]').should(have.text(customer.title))
        return self

    def check_authorization_status_negative(self):
        with allure.step("Проверка авторизации (негативный кейс)"):
            browser.element('.ControlInput_input__error__0DtKl').should(
                have.text('Неверное сочетание логина и пароля'))
        return self

    def search_product_using_title(self, product):
        with allure.step("Выполение поиска продукта по названию"):
            # browser.element('[data-testid="search__button"]').should(be.visible).type(product.title).press_enter()
            browser.element('[data-testid="search__button"]').should(be.visible).clear().type(product.title)
            browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    def check_searched_product_title_in_search_results(self, product):
        with allure.step("Проверка наличия искомого по названию продукта в результатах поиска"):
            browser.element('[data-testid="art__title"]').should(have.text(f'{product.title}'))
        return self


home_page = HomePage()
