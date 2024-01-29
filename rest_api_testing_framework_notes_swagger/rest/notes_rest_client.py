from rest_api_testing_framework_notes_swagger.rest.base_rest_client import (
    BaseRestClient,
)


class NotesRestClient(BaseRestClient):
    """
    Notes REST API service
    """

    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}

    def get_health_check(self, expected_status_code=200):
        """
        Send a GET request to /health-check
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Sending request to check if the server is running and healthy")
        response = self._get("health-check", expected_status_code=expected_status_code)
        return response

    def post_users_register(self, user_name, email, password, expected_status_code=201):
        """
        Send a POST request to /users/register
        :param user_name: user_name
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Register new user as {user_name}")
        response = self._post(
            "users/register",
            json={"name": user_name, "email": email, "password": password},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_login(self, email, password, expected_status_code=200):
        """
        Send a POST request to /users/login
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Login on the website as a {email}")
        response = self._post(
            "users/login",
            json={"email": email, "password": password},
            expected_status_code=expected_status_code,
        )
        if response["status"] == 200:
            self._token = response["data"]["token"]
        return response

    def get_users_profile(self, expected_status_code=200):
        """
        Send a GET request to /users/profile
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Get a user profile")
        response = self._get("users/profile", expected_status_code=expected_status_code)
        return response

    def delete_users_delete_account(self, expected_status_code=200):
        """
        Send a DELETE request to /users/delete-account
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Delete a user's account")
        response = self._delete(
            "users/delete-account", expected_status_code=expected_status_code
        )
        return response

    def patch_users_profile(
        self,
        user_name=None,
        user_phone=None,
        user_company=None,
        expected_status_code=200,
    ):
        """
        Send a PATCH request to /users/profile
        :param user_name: user_name
        :param user_phone: user_phone
        :param user_company: company
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(
            f"Update the user's information such as: {user_name}, {user_phone}, {user_company}"
        )
        response = self._patch(
            "users/profile",
            data={"name": user_name, "phone": user_phone, "company": user_company},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_forgot_password(self, user_email=None, expected_status_code=200):
        """
        Send a POST request to /users/forgot-password
        :param user_email: user_email
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"User: {user_email} forgot password")
        response = self._post(
            "users/forgot-password",
            data={"email": user_email},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_verify_reset_password_token(
        self, token=None, expected_status_code=200
    ):
        """
        Send a POST request to /users/verify-reset-password-token
        :param token: token
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Verify that the provided password reset {token}")
        response = self._post(
            "users/verify-reset-password-token",
            data={"token": token},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_reset_password(self, token, new_password, expected_status_code=200):
        """
        Send a POST request to /users/reset-password
        :param token: token
        :param new_password: new_password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("reset password")
        response = self._post(
            "users/reset-password",
            data={"token": token, "newPassword": new_password},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_change_password(
        self, password, new_password, expected_status_code=200
    ):
        """
        Send a POST request to /users/change-password
        :param password: password
        :param new_password: new_password
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info(
            "Change a user's password by providing the user's current password and the new password."
        )
        response = self._post(
            "users/change-password",
            data={"currentPassword": password, "newPassword": new_password},
            expected_status_code=expected_status_code,
        )
        return response

    def delete_users_logout(self, expected_status_code=200):
        """
        Send a DELETE request to /users/logout
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info(
            "Log out the currently authenticated user by invalidating their token."
        )
        response = self._delete(
            "users/logout", expected_status_code=expected_status_code
        )
        if response["status"] == 200:
            self._token = None
        return response

    def post_notes(
        self, title=None, description=None, category=None, expected_status_code=200
    ):
        """
        Send a Post request to /notes
        :param category: category
        :param title: title
        :param description: description
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info(
            f"Creates a new note with the given {title}, {description}, {category}"
        )
        response = self._post(
            "notes",
            data={"title": title, "description": description, "category": category},
            expected_status_code=expected_status_code,
        )
        return response

    def get_notes(self, expected_status_code=200):
        """
        Send a GET request to /notes
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("Retrieve a list of notes for the authenticated user")
        response = self._get("notes", expected_status_code=expected_status_code)
        return response

    def get_notes_by_id(self, _id=None, expected_status_code=200):
        """
        Send a GET request to /notes/{_id}
        :param _id: id
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info(f"Retrieve a note by its {_id}")
        response = self._get(f"notes/{_id}", expected_status_code=expected_status_code)
        return response

    def put_notes_by_id(
        self,
        _id=None,
        title=None,
        description=None,
        status=None,
        category=None,
        expected_status_code=200,
    ):
        """
        Send a PUT request to /notes/{id}
        :param _id: id
        :param title: title
        :param description: description
        :param status: status
        :param category: category
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("Update an existing note by its id")
        response = self._put(
            f"notes/{_id}",
            data={
                "title": title,
                "description": description,
                "completed": status,
                "category": category,
            },
            expected_status_code=expected_status_code,
        )
        return response

    def patch_notes_by_id(self, _id=None, status=None, expected_status_code=200):
        """
        Send a PATCH request to /notes/{id}
        :param _id: id
        :param status: status
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("Update the complete status of a note by id")
        response = self._patch(
            f"notes/{_id}",
            data={"completed": status},
            expected_status_code=expected_status_code,
        )
        return response

    def delete_notes_by_id(self, _id=None, expected_status_code=200):
        """
        Send a DELETE request to /notes/{id}
        :param _id: id
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("Delete a note by id")
        response = self._delete(
            f"notes/{_id}", expected_status_code=expected_status_code
        )
        return response
