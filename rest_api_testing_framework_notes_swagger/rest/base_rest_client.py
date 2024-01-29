import requests
from logging import getLogger


class BaseRestClient:
    """
    Base class with the logic for the REST API
    """

    BASE_URL: str
    _headers: dict

    def __init__(self):
        self._log = getLogger(__name__)

    def _get(self, path, params=None, headers=None, expected_status_code=200, **kwargs):
        """
        Send GET request to REST API
        :param path: str path that will be added to base api address
        :param params: params for GET request
        :param headers: dictionary of HTTP Headers
        :param expected_status_code: expected response code
        :param kwargs: other params for GET request
        :return: Response in JSON format
        """
        url = self.BASE_URL + path
        headers = headers or self._headers
        self._log.info(f"Send GET request to {url} with params: {params}")
        response = requests.get(url, params, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()

    def _post(
        self,
        path,
        data=None,
        json=None,
        headers=None,
        expected_status_code=200,
        **kwargs,
    ):
        """
        Send POST request to REST API
        :param path: str path that will be added to base api address
        :param data: data for POST request
        :param json: json data for POST request
        :param headers: dictionary of HTTP Headers
        :param expected_status_code: expected response code
        :param kwargs: other params for POST request
        :return: Response in JSON format
        """
        url = self.BASE_URL + path
        headers = headers or self._headers
        self._log.info(f"Send POST request to {url} with data: {data} and json: {json}")
        response = requests.post(url, data, json, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()

    def _delete(self, path, headers=None, expected_status_code=200, **kwargs):
        """
        Send DELETE request to REST API
        :param path: str path that will be added to base api address
        :param headers: dictionary of HTTP Headers
        :param expected_status_code: expected response code
        :param kwargs: other params for DELETE request
        :return: Response in JSON format
        """
        url = self.BASE_URL + path
        headers = headers or self._headers
        self._log.info(f"Send DELETE request to {url}")
        response = requests.delete(url, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()

    def _patch(self, path, data=None, headers=None, expected_status_code=200, **kwargs):
        """
        Send PATCH request to REST API
        :param path: str path that will be added to base api address
        :param data: data for PATCH request
        :param headers: dictionary of HTTP Headers
        :param expected_status_code: expected response code
        :param kwargs: other params for PATCH request
        :return: Response in JSON format
        """
        url = self.BASE_URL + path
        headers = headers or self._headers
        self._log.info(f"Send PATCH request to {url} with data: {data}")
        response = requests.patch(url, data, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()

    def _put(self, path, data=None, headers=None, expected_status_code=200, **kwargs):
        """
        Send PUT request to REST API
        :param path: str path that will be added to base api address
        :param data: data for PATCH request
        :param headers: dictionary of HTTP Headers
        :param expected_status_code: expected response code
        :param kwargs: other params for PUT request
        :return: Response in JSON format
        """
        url = self.BASE_URL + path
        headers = headers or self._headers
        self._log.info(f"Send PUT request to {url} with data: {data}")
        response = requests.put(url, data, headers=headers, **kwargs)
        assert response.status_code == expected_status_code
        return response.json()
