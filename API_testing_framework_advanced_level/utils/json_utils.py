import json
from typing import List

from data.data_classes.country import Country
from utils.file_utils import read_test_data_file


def json_to_country(json_str) -> Country:
    """Convert a JSON string into an object of the Country class"""
    country_dict = json.loads(json_str)
    return Country.from_dict(country_dict)


def json_file_to_country(file_path) -> Country:
    """Convert a JSON file into an object of the Country class"""
    json_str = read_test_data_file(file_path)
    return json_to_country(json_str)


def json_file_to_countries(file_path) -> List:
    """Convert a JSON file into a list if objects of the Country class"""
    json_str = read_test_data_file(file_path)
    json_dict = json.loads(json_str)
    return [Country.from_dict(country) for country in json_dict]


def str_to_json(json_str):
    """Convert a string into a JSON object"""
    return json.loads(json_str)
