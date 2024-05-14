import allure
import jsonschema
from allure_commons.types import Severity

from project_diploma.schemes.scheme_loader import load_scheme
from project_diploma.utils.requests_api import api_post
from tests.REST.conftest import email, password, wrong_password


@allure.epic('Auth')
@allure.label("owner", "Bykat")
@allure.feature("Authorization via REST - POSITIVE case")
@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('layer', 'REST')
def test_auth_with_right_pass_via_rest():
    scheme = load_scheme('auth_post_pass.json')
    url = "/auth/login"
    result = api_post(url, json={"login": email, "password": password})
    assert result.status_code == 200
    jsonschema.validate(result.json(), scheme)
    assert result.json()['error'] is None


@allure.epic('Auth')
@allure.label("owner", "Bykat")
@allure.feature("Authorization via REST - NEGATIVE case")
@allure.tag('API')
@allure.severity(Severity.NORMAL)
@allure.label('layer', 'REST')
def test_auth_with_wrong_pass():
    scheme = load_scheme('auth_post_fail.json')
    url = "/auth/login"
    result = api_post(url, json={"login": email, "password": wrong_password})
    assert result.status_code == 401
    jsonschema.validate(result.json(), scheme)
    assert result.json()['error']['type'] == "Unauthorized"
    assert result.json()['error']['title'] == "Incorrect user data"
