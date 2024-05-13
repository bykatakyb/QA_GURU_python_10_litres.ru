import allure
from allure_commons.types import Severity

from project_diploma.data.data_customer import Customer
from project_diploma.pages.web.basket_page import basket_page
from project_diploma.pages.web.home_page import home_page


@allure.epic('Basket')
@allure.label("owner", "Bykat")
@allure.feature("Basket is empty by default")
@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'UI')
def test_basket_is_empty_for_unauthorized_visitor():
    home_page.open()
    basket_page.open()
    basket_page.check_that_basket_is_empty()


@allure.epic('Basket')
@allure.label("owner", "Bykat")
@allure.feature("Basket is empty by default")
@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'UI')
def test_basket_is_empty_for_authorized_customer():
    customer = Customer(name='bukatovvs',
                        email='bukatovvs@gmail.com',
                        password='LITRESlitres1234')

    home_page.open()
    home_page.do_authorization(customer)
    home_page.check_authorization_status_positive(customer)
    basket_page.open()
    basket_page.check_that_basket_is_empty()
