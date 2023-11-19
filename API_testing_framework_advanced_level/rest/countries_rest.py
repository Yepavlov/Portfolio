from typing import List

from data.data_classes.country import Country
from rest.rest_client import RestClient


class CountriesRest(RestClient):
    """
    Country API service
    """
    BASE_URL = "https://restcountries.com/v3.1/"
    _headers = {'Content-Type': 'application/json'}

    def get_country_by_name(self, country_name, fields=None, expected_status_code=200) -> Country:
        self._log.info("Getting country by name")
        url = f"name/{country_name}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return Country.from_dict(response[0])
        raise ValueError(f"Country with name {country_name} not found")

    def get_country_by_code(self, country_code, fields=None, expected_status_code=200):
        self._log.info("Getting country by code")
        url = f"alpha/{country_code}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return Country.from_dict(response[0])
        raise ValueError(f"Country with code {country_code} not found")

    def get_country_by_codes(self, country_codes, fields=None, expected_status_code=200) -> List:
        self._log.info("Getting countries by codes")
        url = f"alpha?codes={country_codes}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with codes {country_codes} not found")

    def get_countries_by_currency(self, country_currency, fields=None, expected_status_code=200) -> List:
        self._log.info("Getting countries by currency")
        url = f"currency/{country_currency}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with currency {country_currency} not found")

    def get_countries_by_language(self, country_language, fields=None, expected_status_code=200) -> List:
        self._log.info("Getting countries by language")
        url = f"lang/{country_language}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with language {country_language} not found")

    def get_country_by_capital_city(self, capital_city, fields=None, expected_status_code=200) -> Country:
        self._log.info("Getting country by capital city")
        url = f"capital/{capital_city}"
        if fields:
            url += f"?fields={','.join(fields)}"
        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return Country.from_dict(response[0])
        raise ValueError(f"Country with capital city {capital_city} not found")

