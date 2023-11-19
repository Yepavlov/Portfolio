import pytest
from utils.json_utils import json_file_to_country, json_file_to_countries


@pytest.mark.parametrize("country_name, expected_response_file", [
    ("Ukraine", "expected_country_by_name_ukraine.json"),
    ("Germany", "expected_germany.json"),
    ("USA", "expected_usa.json")
])
def test_country_by_name(countries_service, country_name, expected_response_file):
    expected_country = json_file_to_country(expected_response_file)
    actual_country = countries_service.get_country_by_name(country_name)
    assert actual_country == expected_country


@pytest.mark.parametrize("country_code", ["UA", "804", "UKR"])
def test_country_by_code(countries_service, country_code):
    expected_country = json_file_to_country("expected_country_by_name_ukraine.json")
    actual_country = countries_service.get_country_by_code(country_code)
    assert actual_country == expected_country


@pytest.mark.parametrize("country_codes", ["UA,US,DE", "804,840,276", "UKR,USA,DEU"])
def test_countries_by_codes(countries_service, country_codes):
    country_names = ["expected_country_by_name_ukraine.json", "expected_usa.json", "expected_germany.json"]
    expected_countries = [json_file_to_country(country_name) for country_name in country_names]
    actual_countries = countries_service.get_country_by_codes(country_codes)
    for country in expected_countries:
        assert country in actual_countries


@pytest.mark.parametrize("country_path, currency", [
    ("expected_country_by_name_ukraine.json", "UAH"),
    ("expected_germany.json", "EUR"),
    ("expected_usa.json", "USD")
])
def test_countries_by_currency(countries_service, country_path, currency):
    expected_country = json_file_to_country(country_path)
    actual_countries = countries_service.get_countries_by_currency(currency)
    assert expected_country in actual_countries

@pytest.mark.parametrize("country_path, language", [
    ("expected_country_by_name_ukraine.json", "Ukrainian"),
    ("expected_country_by_name_ukraine.json", "Ukr"),
    ("expected_germany.json", "deu"),
    ("expected_turkey.json", "turkish"),
    ("expected_cyprus.json", "turkish")
])
def test_country_by_language(countries_service, country_path, language):
    expected_country = json_file_to_country(country_path)
    actual_countries = countries_service.get_countries_by_language(language)
    assert expected_country in actual_countries


@pytest.mark.parametrize("file_path, language", [
    ("expected_countries_by_language_spanish.json", "spanish"),
    ("expected_country_names_by_language_english.json", "english")
])
def test_countries_by_language(countries_service, file_path, language):
    expected_countries = json_file_to_countries(file_path)
    actual_countries = countries_service.get_countries_by_language(language)
    assert expected_countries == actual_countries


@pytest.mark.parametrize("country_path, capital_city", [
    ("expected_country_by_name_ukraine.json", "Kyiv"),
    ("expected_germany.json", "Berlin"),
    ("expected_turkey.json", "Ankara")
])
def test_countries_by_capital(countries_service, country_path, capital_city):
    expected_country = json_file_to_country(country_path)
    actual_country = countries_service.get_country_by_capital_city(capital_city)
    assert expected_country == actual_country
