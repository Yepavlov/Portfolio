import pytest

from API_testing_framework_with_Allure_report.rest.lambdatest import LambdaTestService


@pytest.fixture(scope="session")
def lambda_test_service():
    return LambdaTestService()
