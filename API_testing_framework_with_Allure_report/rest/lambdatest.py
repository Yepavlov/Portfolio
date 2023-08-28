import json

import requests

import allure


class LambdaTestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    @allure.step("Send a POST request to {path}")
    def _send_request(self, path, input_key, input_str):
        url = self.BASE_URL + path
        response = requests.post(url, data={input_key: input_str})
        allure.attach(url, "Full url", allure.attachment_type.TEXT)
        return response

    @allure.step("Send a POST request to convert JSON to XML")
    def convert_json_to_xml(self, input_str: str) -> str:
        response = self._send_request("json-to-xml", "input-str", input_str).text
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output XML", allure.attachment_type.XML)
        return response

    allure.step("Send a POST request to minify XML")

    def minify_xml(self, input_str: str) -> str:
        response = self._send_request("minify-xml", "input-str", input_str).json()[
            "minify_data"
        ]
        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output minify XML", allure.attachment_type.XML)
        return response

    allure.step("Send a POST request to extract text to JSON")

    def extract_text_from_json(self, input_str: str) -> str:
        response = self._send_request(
            "extract-text-json", "input-str", input_str
        ).json()["data"]
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Extracted TEXT", allure.attachment_type.TEXT)
        return response

    allure.step("Send a POST request to Yaml validator")

    def yaml_validator(self, input_str: str) -> str:
        response = self._send_request("yaml-validator", "yaml-str", input_str).json()[
            "message"
        ]
        allure.attach(input_str, "Input Yaml", allure.attachment_type.YAML)
        allure.attach(response, "Output answer", allure.attachment_type.TEXT)
        return response

    allure.step("Send a POST request to convert JSON to YAML")

    def convert_json_to_yaml(self, input_str: str) -> str:
        response = self._send_request("json-to-yaml", "json-str", input_str).json()[
            "data"
        ]
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    @allure.step("Send a POST request to convert XML to YAML")
    def convert_xml_to_yaml(self, input_str: str) -> str:
        response = self._send_request("xml-to-yaml", "xml-str", input_str).json()[
            "data"
        ]
        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    allure.step("Send a POST request to convert YAML to JSON")

    def convert_yaml_to_json(self, input_str: str) -> str:
        response = self._send_request("yaml-to-json", "yaml-str", input_str).json()
        response_data = response.get("data")

        allure.attach(input_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(
            json.dumps(response_data), "Output JSON", allure.attachment_type.TEXT
        )
        return response_data
