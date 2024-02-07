import os
from logging import getLogger

import pytest

from rest_api_testing_framework_notes_swagger.rest.notes_rest_client import (
    NotesRestClient,
)
from dotenv import load_dotenv

load_dotenv()

logger = getLogger(__name__)


@pytest.fixture(scope="session")
def user_name_notes():
    return os.getenv("USERS_NAME_NOTES")


@pytest.fixture(scope="session")
def email_address_notes():
    return os.getenv("USERS_EMAIL_ADDRESS_NOTES")


@pytest.fixture(scope="session")
def password_notes():
    return os.getenv("USERS_PASSWORD_NOTES")


@pytest.fixture(scope="session")
def new_password_notes():
    return os.getenv("NEW_USERS_PASSWORD_NOTES")


@pytest.fixture
def notes_rest_client():
    return NotesRestClient()


@pytest.fixture
def registered_user(
    notes_rest_client, user_name_notes, email_address_notes, password_notes
):
    notes_rest_client.post_users_register(
        user_name_notes, email_address_notes, password_notes
    )
    yield notes_rest_client
    notes_rest_client.post_users_login(email_address_notes, password_notes)
    notes_rest_client.delete_users_delete_account()


@pytest.fixture
def authenticated_user(
    notes_rest_client, user_name_notes, email_address_notes, password_notes
):
    notes_rest_client.post_users_register(
        user_name_notes, email_address_notes, password_notes
    )
    notes_rest_client.post_users_login(email_address_notes, password_notes)
    yield notes_rest_client
    notes_rest_client.delete_users_delete_account()


@pytest.fixture
def created_notes(authenticated_user):
    authenticated_user.post_notes("Test_title", "Test_description", "Home")
    authenticated_user.post_notes("Test_title_1", "Test_description_1", "Work")
    return authenticated_user
