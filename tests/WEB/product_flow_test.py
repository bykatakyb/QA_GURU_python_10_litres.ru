import allure
from allure_commons.types import Severity

from litres_testing_project.data.data_product import product2, product3
from litres_testing_project.pages.web.basket_page import basket_page
from litres_testing_project.pages.web.product_page import product_page


@allure.epic('Product flow')
@allure.label("owner", "Bykat")
@allure.feature("Adding product to basket ")
@allure.tag('WEB')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'UI')
def test_add_product_to_basket():
    product_page.open(product2)
    product_page.add_product_to_basket()
    basket_page.open()
    basket_page.check_added_product_inside_basket(product2)
    basket_page.delete_product_from_basket()


@allure.epic('Product flow')
@allure.label("owner", "Bykat")
@allure.feature("Kicking product from basket ")
@allure.tag('WEB')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'UI')
def test_delete_product_from_basket():
    product_page.open(product3)
    product_page.add_product_to_basket()
    basket_page.open()
    basket_page.delete_product_from_basket()
    basket_page.check_that_basket_is_empty()
