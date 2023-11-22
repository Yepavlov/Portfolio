from logging import getLogger

import requests
import allure

class RestClient:
    """
    Basic class with the logic for REST API
    """
    BASE_URL: str
    _headers: dict

    def __init__(self):
        self._log = getLogger(__name__)


    @allure.step("Send Get request to {path}")
    @allure.link("{BASE_URL}", name="API Base URL")
    def _get(self, path, params=None, headers=None, expected_status_code=200, **kwargs):
        """
        Send a GET request to REST API
        :param path: str path that will be added to BASE_URL address
        :param params: params for GET request
        :param headers: dictionary of HTTP headers
        :param expected_status_code: expected response code
        :param kwargs: other params for GET request
        :return: response in JSON format
        """
        url = self.BASE_URL + path
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        headers = headers or self._headers
        self._log.info(f"GET request to {url} with params: {params}")
        response = requests.get(url, params, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()

    @allure.step("Send POST request to {path}")
    @allure.link("{BASE_URL}", name="API Base URL")
    def _post(self, path, data=None, json=None, headers=None, expected_status_code=200, **kwargs):
        """
        Send a POST request to REST API
        :param path: str path that will be added to BASE_URL address
        :param data: data for POST request
        :param json: json data for POST request
        :param headers: dictionary of HTTP headers
        :param expected_status_code: expected response code
        :param kwargs: other params for POST request
        :return: response in JSON format
        """
        url = self.BASE_URL + path
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        headers = headers or self._headers
        self._log.info(f"POST request to {url} with data: {data} and json: {json}")
        response = requests.post(url, data, json, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()
