import allure
from allure_commons.types import Severity

from litres_testing_project.data.data_customer import Customer
from litres_testing_project.pages.web.basket_page import basket_page
from litres_testing_project.pages.web.home_page import home_page


@allure.epic('Basket')
@allure.label("owner", "Bykat")
@allure.feature("Basket have promo banner")
@allure.tag('WEB')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'UI')
def test_basket_have_promo():
    basket_page.open()
    basket_page.check_promo_inside_basket()


@allure.epic('Basket')
@allure.label("owner", "Bykat")
@allure.feature("Basket is empty by default (unauthorized)")
@allure.tag('WEB')
@allure.severity(Severity.MINOR)
@allure.label('layer', 'UI')
def test_basket_is_empty_for_unauthorized_visitor():
    home_page.open()
    basket_page.open()
    basket_page.check_that_basket_is_empty()


@allure.epic('Basket')
@allure.label("owner", "Bykat")
@allure.feature("Basket is empty by default (authorized)")
@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'UI')
def test_basket_is_empty_for_authorized_customer():
    customer = Customer(name='bukatovvs',
                        email='bukatovvs@gmail.com',
                        password='LITRESlitres1234')

    home_page.open()
    home_page.do_authorization(customer)
    basket_page.open()
    basket_page.check_that_basket_is_empty()
