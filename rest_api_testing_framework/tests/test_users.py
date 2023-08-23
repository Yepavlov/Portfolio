def test_users_register(notes_service, email, password):
    response = notes_service.post_users_register("Yevhenii", email, password)
    assert response["data"]["email"] == email
    notes_service.post_users_login(email, password)
    notes_service.delete_users_delete_users_account()


def test_users_login(notes_service, email, password):
    notes_service.post_users_register("Yevhenii", email, password)
    response = notes_service.post_users_login(email, password)
    assert response["data"]["token"] is not None
    notes_service.delete_users_delete_users_account()


def test_users_login_with_invalid_email(registered_notes_service, password):
    response = registered_notes_service.post_users_login(
        "invalid@email.com", password, expected_status_code=401
    )
    assert response["message"] == "Incorrect email address or password"


def test_users_login_with_invalid_password(registered_notes_service, email):
    response = registered_notes_service.post_users_login(
        email, "invalid2023", expected_status_code=401
    )
    assert response["message"] == "Incorrect email address or password"


def test_get_users_profile(authenticated_notes_service):
    response = authenticated_notes_service.get_users_profile()
    assert response["message"] == "Profile successful"


def test_patch_users_profile(authenticated_notes_service):
    response = authenticated_notes_service.patch_users_profile(
        "Yevhenii", "+380509379992", "Toyota"
    )
    assert response["data"]["name"] == "Yevhenii"
    assert response["data"]["phone"] == "+380509379992"
    assert response["data"]["company"] == "Toyota"


def test_users_profile_with_empty_field(authenticated_notes_service):
    response = authenticated_notes_service.patch_users_profile("Kolya", "", "")
    assert response["data"]["name"] == "Kolya"
    assert response["data"]["phone"] == ""
    assert response["data"]["company"] == ""


def test_users_forgot_password(registered_notes_service, email):
    response = registered_notes_service.post_users_forgot_password(email)
    assert (
        response["message"]
        == f"Password reset link successfully sent to {email}. Please verify by clicking on the given link"
    )


def test_users_change_password(authenticated_notes_service, password, new_password):
    response = authenticated_notes_service.post_users_change_password(
        password, new_password
    )
    assert response["message"] == "The password was successfully updated"


def test_users_logout(
    notes_service, authenticated_notes_service_without_delete, email, password
):
    response = authenticated_notes_service_without_delete.delete_users_logout()
    assert response["message"] == "User has been successfully logged out"
    notes_service.post_users_login(email, password)
    notes_service.delete_users_delete_users_account()


def test_users_delete_account(authenticated_notes_service_without_delete):
    response = (
        authenticated_notes_service_without_delete.delete_users_delete_users_account()
    )
    assert response["message"] == "Account successfully deleted"
