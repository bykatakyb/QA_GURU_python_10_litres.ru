import allure
from allure_commons.types import Severity

from project_diploma.data.data_product import product
from project_diploma.pages.web.home_page import home_page


# from selene import browser, be


@allure.epic('Product Search')
@allure.label("owner", "Bykat")
@allure.feature("Product Search on the home page by title")
@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'UI')
def test_product_search_by_title():
    home_page.open()
    home_page.search_product_using_title(product)
    home_page.check_searched_product_title_in_search_results(product)
