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
            browser.element('span[class="user_header__name"]').should(have.text(customer.name))
        return self

    def check_authorization_status_negative(self):
        with allure.step("Проверка авторизации (негативный кейс)"):
            browser.element('.ControlInput_input__error__0DtKl').should(
                have.text('Неверное сочетание логина и пароля'))
        return self


home_page = HomePage()
