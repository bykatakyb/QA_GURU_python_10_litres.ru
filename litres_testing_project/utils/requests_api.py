import allure
import requests

from litres_testing_project.utils.logging_api import logging_api
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


def api_put(url, **kwargs):
    with allure.step("PUT запрос"):
        result = requests.put(base_url + url, **kwargs)
        logging_api(result)
        return result
