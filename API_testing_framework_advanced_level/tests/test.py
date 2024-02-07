import pytest
from API_testing_framework_advanced_level.utils.json_utils import json_file_to_country, json_file_to_countries
import allure


@allure.suite("Countries API tests")
@allure.title("Test Get country by name")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get country by name" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get country by name.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_name, expected_response_file", [
    ("Ukraine", "expected_country_by_name_ukraine.json"),
    ("Germany", "expected_germany.json"),
    ("USA", "expected_usa.json")
])
def test_country_by_name(countries_service, country_name, expected_response_file):
    with allure.step("Prepare expected test data."):
        expected_country = json_file_to_country(expected_response_file)

    with allure.step("Send request and get country by name."):
        actual_country = countries_service.get_country_by_name(country_name)

    with allure.step("Compare expected and actual result."):
        assert actual_country == expected_country


@allure.suite("Countries API tests")
@allure.title("Test Get country by code")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get country by code" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get country by code.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_code", ["UA", "804", "UKR"])
def test_country_by_code(countries_service, country_code):
    with allure.step("Prepare expected test data."):
        expected_country = json_file_to_country("expected_country_by_name_ukraine.json")

    with allure.step("Send request and get country by code."):
        actual_country = countries_service.get_country_by_code(country_code)

    with allure.step("Compare expected and actual result."):
        assert actual_country == expected_country


@allure.suite("Countries API tests")
@allure.title("Test Get country by codes")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get country by codes" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get country by codes.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_codes", ["UA,US,DE", "804,840,276", "UKR,USA,DEU"])
def test_countries_by_codes(countries_service, country_codes):
    with allure.step("Prepare expected test data."):
        country_names = ["expected_country_by_name_ukraine.json", "expected_usa.json", "expected_germany.json"]
        expected_countries = [json_file_to_country(country_name) for country_name in country_names]
    with allure.step("Send request and get country by codes."):
        actual_countries = countries_service.get_country_by_codes(country_codes)
    with allure.step("Compare expected and actual result."):
        for country in expected_countries:
            assert country in actual_countries


@allure.suite("Countries API tests")
@allure.title("Test Get countries by currency")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get countries by currency" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get countries by currency.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_path, currency", [
    ("expected_country_by_name_ukraine.json", "UAH"),
    ("expected_germany.json", "EUR"),
    ("expected_usa.json", "USD")
])
def test_countries_by_currency(countries_service, country_path, currency):
    with allure.step("Prepare expected test data."):
        expected_country = json_file_to_country(country_path)
    with allure.step("Send request and get countries by currency."):
        actual_countries = countries_service.get_countries_by_currency(currency)
    with allure.step("Compare expected and actual result."):
        assert expected_country in actual_countries


@allure.suite("Countries API tests")
@allure.title("Test Get country by language")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get country by language" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get country by language.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_path, language", [
    ("expected_country_by_name_ukraine.json", "Ukrainian"),
    ("expected_country_by_name_ukraine.json", "Ukr"),
    ("expected_germany.json", "deu"),
    ("expected_turkey.json", "turkish"),
    ("expected_cyprus.json", "turkish")
])
def test_country_by_language(countries_service, country_path, language):
    with allure.step("Prepare expected test data."):
        expected_country = json_file_to_country(country_path)
    with allure.step("Send request and get country by language."):
        actual_countries = countries_service.get_countries_by_language(language)
    with allure.step("Compare expected and actual result."):
        assert expected_country in actual_countries


@allure.suite("Countries API tests")
@allure.title("Test Get countries by language")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get countries by language" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get countries by language.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("file_path, language", [
    ("expected_countries_by_language_spanish.json", "spanish"),
    ("expected_country_names_by_language_english.json", "english")
])
def test_countries_by_language(countries_service, file_path, language):
    with allure.step("Prepare expected test data."):
        expected_countries = json_file_to_countries(file_path)
    with allure.step("Send request and get countries by language."):
        actual_countries = countries_service.get_countries_by_language(language)
    with allure.step("Compare expected and actual result."):
        assert expected_countries == actual_countries


@allure.suite("Countries API tests")
@allure.title("Test Get country by capital")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    This test case verifies that the API request "get country by capital" works correctly.
    Steps:
    1. Prepare expected test data.
    2. Send request and get country by capital.
    3. Compare expected and actual result.
""")
@pytest.mark.parametrize("country_path, capital_city", [
    ("expected_country_by_name_ukraine.json", "Kyiv"),
    ("expected_germany.json", "Berlin"),
    ("expected_turkey.json", "Ankara")
])
def test_countries_by_capital(countries_service, country_path, capital_city):
    with allure.step("Prepare expected test data."):
        expected_country = json_file_to_country(country_path)
    with allure.step("Send request and get country by capital."):
        actual_country = countries_service.get_country_by_capital_city(capital_city)
    with allure.step("Compare expected and actual result."):
        assert expected_country == actual_country
