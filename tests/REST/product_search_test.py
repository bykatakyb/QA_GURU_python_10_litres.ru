import allure
import jsonschema
from allure_commons.types import Severity

from litres_testing_project.schemes.scheme_loader import load_scheme
from litres_testing_project.utils.requests_api import api_get


@allure.epic('Product Search')
@allure.label("owner", "Bykat")
@allure.feature("Product Search by title via REST - POSITIVE case")
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'REST')
def test_product_search_by_existed_title_via_rest():
    scheme = load_scheme('product_search_get_pass.json')
    book_title = 'Разговоры с друзьями'
    art_types = 'text_book'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "art_types": art_types, "types": types}
    result = api_get(url, params=params)
    assert result.status_code == 200
    assert result.json()['payload']['data'][0]['type'] == "text_book"


@allure.epic('Product Search')
@allure.label("owner", "Bykat")
@allure.feature("Product Search by title via REST - NEGATIVE case")
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('layer', 'REST')
def test_product_search_by_nonexistent_title_via_rest():
    scheme = load_scheme('product_search_get_fail.json')
    book_title = 'йцукенфывап'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "types": types}
    result = api_get(url, params=params)
    assert result.status_code == 200
    jsonschema.validate(result.json(), scheme)
    assert len(result.json()['payload']['data']) == 0
