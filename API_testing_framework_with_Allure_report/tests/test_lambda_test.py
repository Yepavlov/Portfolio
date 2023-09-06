import json

import allure
import pytest

from API_testing_framework_with_Allure_report.utils.file_utils import read_data_file


@allure.suite("Lambda_test API tests")
@allure.title("Testing convert JSON to XML")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-xml-converter")
@allure.description(
    """
    This test case verifies that the API endpoint "Convert JSON to XML" works correctly.
    Steps:
    1. Prepare test data and convert expected_xml to minify view.
    2. Convert JSON to XML and convert actual_xml to minify view via API.
    3. Compare minify_xml and minify_actual_xml.
    """
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_convert_json_to_xml(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        minify_xml = lambda_test_service.minify_xml(expected_xml)

    with allure.step("Convert JSON to XML via API"):
        actual_xml = lambda_test_service.convert_json_to_xml(input_json)
        minify_actual_xml = lambda_test_service.minify_xml(actual_xml)

    with allure.step("Compare expected and actual result"):
        assert minify_xml == minify_actual_xml


@allure.suite("Lambda_test API tests")
@allure.title("Testing extract text from JSON")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.lambdatest.com/free-online-tools/extract-text-from-json")
@allure.description(
    """
    This test case verifies that the API endpoint "Extract text fron JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected_text and actual_text
    """
)
@pytest.mark.parametrize("file_name", ["1", "2", "3"])
def test_extract_text_from_json(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_text = read_data_file(f"text/{file_name}.txt")

    with allure.step("Extract text from JSON via API"):
        actual_text = lambda_test_service.extract_text_from_json(input_json)

    with allure.step("Compare expected_text and actual_text"):
        actual_text = actual_text.replace(" \n", "\n")
        assert expected_text == actual_text


@allure.suite("Lambda_test API tests")
@allure.title("Testing YAML validator")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@allure.description(
    """
    This test case verifies that the API endpoint "Testing YAML validator" works correctly.
    Steps:
    1. Prepare test data.
    2. Checking input Yaml data.
    3. Compare text of response and text in expected response
    """
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def testing_yaml_validator(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Checking input Yaml data"):
        response = lambda_test_service.yaml_validator(input_yaml)

    with allure.step("Compare text of response and text in expected response"):
        assert "Valid YAML" == response


@allure.suite("Lambda_test API tests")
@allure.title("Testing YAML validator with incorrect data")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@allure.description(
    """
    This test case verifies that the API endpoint "Testing YAML validator with incorrect data" works correctly.
    Steps:
    1. Prepare test data.
    2. Checking input incorrect Yaml data.
    3. Compare text of response and text in expected response
    """
)
@pytest.mark.parametrize("file_name", ["3", "4"])
def testing_yaml_validator_with_incorrect_data(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Checking input incorrect Yaml data"):
        response = lambda_test_service.yaml_validator(input_yaml)

    with allure.step("Compare text of response and text in expected response"):
        assert "Unable to parse at line" in response


@allure.suite("Lambda_test API tests")
@allure.title("Testing convert JSON to YAML")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@allure.description(
    """
    This test case verifies that the API endpoint "Testing convert JSON to YAML" works correctly.
    Steps:
    1. Prepare test data.
    2. Convert JSON to YAML.
    3. Compare expected_yaml and actual_yaml
    """
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_convert_json_to_yaml(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert JSON to YAML"):
        actual_yaml = lambda_test_service.convert_json_to_yaml(input_json)

    with allure.step("Compare expected_yaml and actual_yaml"):
        assert expected_yaml == actual_yaml


@allure.suite("Lambda_test API tests")
@allure.title("Testing convert XML to YAML")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml")
@allure.description(
    """
    This test case verifies that the API endpoint "Testing convert XML to YAML" works correctly.
    Steps:
    1. Prepare test data.
    2. Convert XML to YAML.
    3. Compare expected_yaml and actual_yaml
    """
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_convert_xml_to_yaml(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert XML to YAML"):
        actual_yaml = lambda_test_service.convert_xml_to_yaml(input_xml)

    with allure.step("Compare expected_yaml and actual_yaml"):
        assert expected_yaml == actual_yaml


@allure.suite("Lambda_test API tests")
@allure.title("Testing convert YAML to JSON")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-to-json")
@allure.description(
    """
    This test case verifies that the API endpoint "Testing convert YAML to JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Convert YAML to JSON.
    3. Compare expected_json and actual_json
    """
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_convert_yaml_to_json(lambda_test_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")
        expected_json_str = read_data_file(f"json/{file_name}.json")
        expected_json = json.loads(expected_json_str)

    with allure.step("Convert YAML to JSON"):
        actual_json = lambda_test_service.convert_yaml_to_json(input_yaml)

    with allure.step("Compare expected_json and actual_json"):
        assert expected_json == actual_json
