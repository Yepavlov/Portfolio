import pytest

from rest.countries_rest import CountriesRest


@pytest.fixture
def countries_service():
    return CountriesRest()
