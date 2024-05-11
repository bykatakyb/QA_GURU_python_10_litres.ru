import allure
from allure_commons.types import Severity

from project_diploma.data.data_customer import Customer
from project_diploma.pages.web.home_page import home_page


@allure.epic('Auth')
@allure.label("owner", "Bykat")
@allure.feature("Authorization - POSITIVE case")
@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
def test_auth_with_right_pass():
    customer = Customer(name='bukatovvs',
                        email='bukatovvs@gmail.com',
                        password='LITRESlitres1234')

    home_page.open()
    home_page.do_authorization(customer)
    home_page.check_authorization_status_positive(customer)


@allure.epic('Auth')
@allure.label("owner", "Bykat")
@allure.feature("Authorization - NEGATIVE case")
@allure.tag('WEB')
@allure.severity(Severity.NORMAL)
def test_auth_with_wrong_pass():
    customer = Customer(name='bukatovvs',
                        email='bukatovvs@gmail.com',
                        password='123Password')

    home_page.open()
    home_page.do_authorization(customer)
    home_page.check_authorization_status_negative()
