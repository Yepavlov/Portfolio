from rest_api_testing_framework.rest.rest_client import RestClient


class NotesRest(RestClient):
    """
    Notes API service
    """

    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}

    def get_health_check(self):
        """
        Send a GET request to /health-check
        :return: response in JSON format
        """
        self._log.info("Sending cheking-health request")
        response = self._get("health-check")
        return response

    def post_users_register(self, name, email, password, expected_status_code=201):
        """
        Send a POST request to /users/register
        :param name: name
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Register in as {name}")
        response = self._post(
            "users/register",
            json={"name": name, "email": email, "password": password},
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
        self._log.info(f"Register in as {email}")
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
        self._log.info("Getting user profile")
        response = self._get("users/profile", expected_status_code=expected_status_code)
        return response

    def patch_users_profile(
        self, name=None, phone=None, company=None, expected_status_code=200
    ):
        """
        Send a PATCH request to /users/profile
        :param name: name
        :param phone: phone
        :param company: company
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("update user info")
        response = self._patch(
            "users/profile",
            data={"name": name, "phone": phone, "company": company},
            expected_status_code=expected_status_code,
        )
        return response

    def post_users_forgot_password(self, email, expected_status_code=200):
        """
        Send a POST request to /users/forgot-password
        :param email: email
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("user forgot password")
        response = self._post(
            "users/forgot-password",
            data={"email": email},
            expected_status_code=expected_status_code,
        )
        return response

    def post_verify_reset_password_token(self, token, expected_status_code=200):
        """
        Send a POST request to /users/verify-reset-password-token
        :param token: token
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("verify reset password token")
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
        self._log.info("change user password")
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
        self._log.info("user logout")
        response = self._delete(
            "users/logout", expected_status_code=expected_status_code
        )
        if response["status"] == 200:
            self._token = None
        return response

    def delete_users_delete_users_account(self, expected_status_code=200):
        """
        Send a DELETE request to /users/delete-account
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("delete a user's account")
        response = self._delete(
            "users/delete-account", expected_status_code=expected_status_code
        )
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
        self._log.info("post notes")
        response = self._post(
            "notes",
            data={"title": title, "description": description, "category": category},
            expected_status_code=expected_status_code,
        )
        return response

    def get_all_notes(self, expected_status_code=200):
        """
        Send a GET request to /notes
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("receive a list of notes")
        response = self._get("notes", expected_status_code=expected_status_code)
        return response

    def get_notes_by_id(self, _id, expected_status_code=200):
        """
        Send a GET request to /notes/{id}
        :param _id: id
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("receive a note by id")
        response = self._get(f"notes/{_id}", expected_status_code=expected_status_code)
        return response

    def put_notes_by_id(
        self,
        _id,
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
        self._log.info(
            "Creates a new note with the given title, description, category and user id"
        )
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

    def patch_notes_by_id(self, _id, status=None, expected_status_code=200):
        """
        Send a PATCH request to /notes/{id}
        :param _id: id
        :param status: status
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info(
            "Update the completed attribute of the note with the specified id"
        )
        response = self._patch(
            f"notes/{_id}",
            data={"completed": status},
            expected_status_code=expected_status_code,
        )
        return response

    def delete_notes_by_id(self, _id, expected_status_code=200):
        """
        Send a DELETE request to /notes/{id}
        :param _id: id
        :param expected_status_code: expected_status_code
        :return: response in JSON format
        """
        self._log.info("Deletes a note with the specified ID")
        response = self._delete(
            f"notes/{_id}", expected_status_code=expected_status_code
        )
        return response
