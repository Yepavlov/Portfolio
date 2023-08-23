import os
from logging import getLogger

import pytest

from rest_api_testing_framework.rest.notes_rest import NotesRest

logger = getLogger(__name__)


@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")


@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def new_password():
    return os.getenv("NEW_PASSWORD")


@pytest.fixture()
def notes_service():
    return NotesRest()


@pytest.fixture()
def registered_notes_service(notes_service, email, password):
    notes_service.post_users_register("Yevhenii", email, password)
    yield notes_service
    notes_service.post_users_login(email, password)
    notes_service.delete_users_delete_users_account()


@pytest.fixture()
def authenticated_notes_service(notes_service, email, password):
    notes_service.post_users_register("Yevhenii", email, password)
    notes_service.post_users_login(email, password)
    yield notes_service
    notes_service.delete_users_delete_users_account()


@pytest.fixture()
def authenticated_notes_service_without_delete(notes_service, email, password):
    notes_service.post_users_register("Yevhenii", email, password)
    notes_service.post_users_login(email, password)
    return notes_service


@pytest.fixture()
def prepared_notes(notes_service, email, password):
    notes_service.post_users_register("Yevhenii", email, password)
    notes_service.post_users_login(email, password)
    logger.info("Preparing note for tests")
    notes_service.post_notes("Test", "Testing notes", "Work")
    notes_service.post_notes("Test2", "Testing notes2", "Home")
    yield notes_service
    notes_service.delete_users_delete_users_account()
