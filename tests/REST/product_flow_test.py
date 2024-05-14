import allure
import jsonschema
from allure_commons.types import Severity

from project_diploma.schemes.scheme_loader import load_scheme
from project_diploma.utils.requests_api import api_put


@allure.epic('Product flow')
@allure.label("owner", "Bykat")
@allure.feature("Adding product to basket via REST")
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'REST')
def test_add_product_to_basket_pass_via_rest():
    scheme = load_scheme('add_product_to_basket_pass.json')
    url = "/cart/arts/add"
    art_ids = [63415002]
    headers = {"Content-Type": "application/json"}
    result = api_put(url, headers=headers, json={"art_ids": art_ids})
    assert result.status_code == 200
    jsonschema.validate(result.json(), scheme)
    assert result.json()['payload']['data']['added_art_ids'] == art_ids
    assert result.json()['payload']['data']['failed_art_ids'] == []
   