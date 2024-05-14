import allure
import jsonschema
from allure_commons.types import Severity

from project_diploma.schemes.scheme_loader import load_scheme
from project_diploma.utils.requests_api import api_post
from tests.REST.conftest import email, password


@allure.epic('Auth')
@allure.label("owner", "Bykat")
@allure.feature("Authorization - POSITIVE case")
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'REST')
def test_auth_for_registered_customer():
    scheme = load_scheme('auth.json')
    url = "/auth/login"

    result = api_post(url, json={"login": email, "password": password})

    assert result.status_code == 200
    jsonschema.validate(result.json(), scheme)
    assert result.json()['error'] is None
