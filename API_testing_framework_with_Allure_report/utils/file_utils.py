import os

import allure


def read_data_file(file_path):
    """Read file in data folder and return its content as string"""
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    file_path = os.path.join(data_folder, file_path)

    with open(file_path, "r", encoding="utf8") as file:
        file_content = file.read()
    allure.attach(
        file_content, "File content", get_attachment_type_by_file_extension(file_path)
    )

    return file_content


def get_attachment_type_by_file_extension(file_path):
    """Return attachment type by file extension."""
    match file_path.split(".")[-1].lower():
        case "json":
            return allure.attachment_type.JSON
        case "xml":
            return allure.attachment_type.XML
        case "yaml":
            return allure.attachment_type.YAML
        case _:
            return allure.attachment_type.TEXT
