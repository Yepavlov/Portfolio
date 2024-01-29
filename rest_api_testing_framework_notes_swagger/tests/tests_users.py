def test_post_users_register(
    notes_rest_client, user_name_notes, email_address_notes, password_notes
):
    response = notes_rest_client.post_users_register(
        user_name_notes, email_address_notes, password_notes
    )
    assert response["message"] == "User account created successfully"
    assert response["data"]["email"] == f"{email_address_notes}"
    notes_rest_client.post_users_login(email_address_notes, password_notes)
    notes_rest_client.delete_users_delete_account()


def test_post_user_login(registered_user, email_address_notes, password_notes):
    response = registered_user.post_users_login(email_address_notes, password_notes)
    assert response["success"] is True
    assert response["data"]["token"] is not None


def test_post_user_login_without_data(registered_user):
    response = registered_user.post_users_login("", "", expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "A valid email address is required"


def test_post_user_login_without_password(registered_user, email_address_notes):
    response = registered_user.post_users_login(
        email_address_notes, "", expected_status_code=400
    )
    assert response["success"] is False
    assert response["message"] == "Password must be between 6 and 30 characters"


def test_post_user_login_invalid_email(registered_user, password_notes):
    response = registered_user.post_users_login(
        "invalid@gmail.com", password_notes, expected_status_code=401
    )
    assert response["success"] is False
    assert response["message"] == "Incorrect email address or password"


def test_get_user_profile(authenticated_user, email_address_notes):
    response = authenticated_user.get_users_profile()
    assert response["success"] is True
    assert response["data"]["email"] == f"{email_address_notes}"


def test_get_user_profile_with_invalid_token(authenticated_user):
    current_token = authenticated_user._token
    authenticated_user._token = (
        "9412f3bb7f4949aaab992acddb9a02b6b417d272cfd84092a371b4b36f24b9c8"
    )
    response = authenticated_user.get_users_profile(expected_status_code=401)
    authenticated_user._token = current_token
    assert response["success"] is False
    assert (
        response["message"]
        == "Access token is not valid or has expired, you will need to login"
    )


def test_get_user_profile_without_token(authenticated_user):
    current_token = authenticated_user._token
    authenticated_user._token = None
    response = authenticated_user.get_users_profile(expected_status_code=401)
    authenticated_user._token = current_token
    assert response["success"] is False
    assert (
        response["message"]
        == "No authentication token specified in x-auth-token header"
    )


def test_patch_users_profile(authenticated_user):
    response = authenticated_user.patch_users_profile(
        "Test_1", "12345678", "Test_company"
    )
    assert response["success"] is True
    assert response["data"]["name"] == "Test_1"
    assert response["data"]["phone"] == "12345678"
    assert response["data"]["company"] == "Test_company"


def test_patch_users_profile_without_user_name(authenticated_user):
    response = authenticated_user.patch_users_profile(
        user_name=None,
        user_phone="12345678",
        user_company="Test_company",
        expected_status_code=400,
    )
    assert response["success"] is False
    assert response["message"] == "User name must be between 4 and 30 characters"


def test_patch_users_profile_without_user_phone(authenticated_user):
    response = authenticated_user.patch_users_profile(
        user_name="Test_1", user_company="Test_company"
    )
    assert response["message"] == "Profile updated successful"
    assert response["data"]["name"] == "Test_1"
    assert response["data"]["company"] == "Test_company"


def test_patch_users_profile_without_user_company(authenticated_user):
    response = authenticated_user.patch_users_profile(
        user_name="Test_1", user_phone="12345678"
    )
    assert response["message"] == "Profile updated successful"
    assert response["data"]["name"] == "Test_1"
    assert response["data"]["phone"] == "12345678"


def test_patch_users_profile_with_short_user_phone(authenticated_user):
    response = authenticated_user.patch_users_profile(
        user_name="Test_1",
        user_phone="1234567",
        user_company="Test_company",
        expected_status_code=400,
    )
    assert response["success"] is False
    assert response["message"] == "Phone number should be between 8 and 20 digits"


def test_post_users_forgot_password(registered_user, email_address_notes):
    response = registered_user.post_users_forgot_password(email_address_notes)
    assert response["success"] is True
    assert (
        response["message"]
        == f"Password reset link successfully sent to {email_address_notes}. "
        f"Please verify by clicking on the given link"
    )


def test_post_users_forgot_password_with_incorrect_email(registered_user):
    response = registered_user.post_users_forgot_password(expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "A valid email address is required"


def test_post_users_verify_reset_password_with_invalid_token(authenticated_user):
    token = authenticated_user._token
    response = authenticated_user.post_users_verify_reset_password_token(
        token, expected_status_code=401
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "The provided password reset token is invalid or has expired"
    )


def test_post_users_change_password(
    authenticated_user, password_notes, new_password_notes
):
    response = authenticated_user.post_users_change_password(
        password_notes, new_password_notes
    )
    assert response["success"] is True
    assert response["message"] == "The password was successfully updated"


def test_users_change_password_with_incorrect_password(
    authenticated_user, new_password_notes
):
    response = authenticated_user.post_users_change_password(
        "incorrect_password", new_password_notes, expected_status_code=400
    )
    assert response["success"] is False
    assert response["message"] == "The current password is incorrect"


def test_delete_users_logout(authenticated_user, email_address_notes, password_notes):
    response = authenticated_user.delete_users_logout()
    assert response["success"] is True
    assert response["message"] == "User has been successfully logged out"
    authenticated_user.post_users_login(email_address_notes, password_notes)


def test_delete_users_delete_account(
    notes_rest_client, user_name_notes, email_address_notes, password_notes
):
    notes_rest_client.post_users_register(
        user_name_notes, email_address_notes, password_notes
    )
    notes_rest_client.post_users_login(email_address_notes, password_notes)
    response = notes_rest_client.delete_users_delete_account()
    assert response["success"] is True
    assert response["message"] == "Account successfully deleted"


def test_delete_users_delete_account_with_invalid_token(authenticated_user):
    current_token = authenticated_user._token
    authenticated_user._token = (
        "25824d617aad4f8b817eea51246612d815b14057167e4a6687ae94d820ac2ec2"
    )
    response = authenticated_user.delete_users_delete_account(expected_status_code=401)
    assert response["success"] is False
    assert (
        response["message"]
        == "Access token is not valid or has expired, you will need to login"
    )
    authenticated_user._token = current_token
