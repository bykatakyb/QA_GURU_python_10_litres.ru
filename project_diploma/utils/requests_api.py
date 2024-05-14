import allure
import requests

from project_diploma.utils.logging_api import logging_api
from tests.REST.conftest import base_url


def api_get(url, **kwargs):
    with allure.step("GET запрос"):
        result = requests.get(base_url + url, **kwargs)
        logging_api(result)
        return result


def api_post(url, **kwargs):
    with allure.step("POST запрос"):
        result = requests.post(base_url + url, **kwargs)
        logging_api(result)
        return result
