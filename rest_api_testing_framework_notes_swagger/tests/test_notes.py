def test_post_notes(authenticated_user):
    response = authenticated_user.post_notes("Test_title", "Test_description", "Home")
    assert response["success"] is True
    assert response["message"] == "Note successfully created"
    assert response["data"]["title"] == "Test_title"
    assert response["data"]["description"] == "Test_description"
    assert response["data"]["category"] == "Home"


def test_post_notes_without_data(authenticated_user):
    response = authenticated_user.post_notes(expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "Title must be between 4 and 100 characters"


def test_post_notes_without_description(authenticated_user):
    response = authenticated_user.post_notes(
        title="Test_title", category="Home", expected_status_code=400
    )
    assert response["success"] is False
    assert response["message"] == "Description must be between 4 and 1000 characters"


def test_post_notes_without_category(authenticated_user):
    response = authenticated_user.post_notes(
        title="Test_title", description="Test_description", expected_status_code=400
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "Category must be one of the categories: Home, Work, Personal"
    )


def test_post_notes_with_invalid_token(authenticated_user):
    current_token = authenticated_user._token
    authenticated_user._token = (
        "fdf374ed410e468a9e9349def4d72228caf45b87a7f3430cadba3b3cb6d660e9"
    )
    response = authenticated_user.post_notes(
        "Test_title", "Test_description", "Home", expected_status_code=401
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "Access token is not valid or has expired, you will need to login"
    )
    authenticated_user._token = current_token


def test_get_notes(created_notes):
    response = created_notes.get_notes()
    assert response["success"] is True
    assert response["message"] == "Notes successfully retrieved"
    assert response["data"][1]["title"] == "Test_title"
    assert response["data"][1]["description"] == "Test_description"
    assert response["data"][1]["category"] == "Home"
    assert response["success"] is True
    assert response["message"] == "Notes successfully retrieved"
    assert response["data"][0]["title"] == "Test_title_1"
    assert response["data"][0]["description"] == "Test_description_1"
    assert response["data"][0]["category"] == "Work"


def test_get_notes_by_id(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.get_notes_by_id(id_notes)
    assert response_got_note["success"] is True
    assert response_got_note["data"]["id"] == id_notes
    assert response_got_note["data"]["title"] == "Test_title"
    assert response_got_note["data"]["description"] == "Test_description"
    assert response_got_note["data"]["category"] == "Home"


def test_get_notes_by_nonexistent_id(created_notes):
    response = created_notes.get_notes_by_id(
        "64298e2b6747aa02118d3c23", expected_status_code=404
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_get_notes_without_note_id(created_notes):
    response = created_notes.get_notes_by_id(expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_put_notes_by_id(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.put_notes_by_id(
        _id=id_notes,
        title="Changed_title",
        description="Changed_description",
        status="true",
        category="Personal",
    )
    assert response_got_note["success"] is True
    assert response_got_note["message"] == "Note successfully Updated"
    assert response_got_note["data"]["id"] == id_notes
    assert response_got_note["data"]["title"] == "Changed_title"
    assert response_got_note["data"]["description"] == "Changed_description"
    assert response_got_note["data"]["category"] == "Personal"
    assert response_got_note["data"]["completed"] is True


def test_put_notes_by_nonexistent_id(created_notes):
    response = created_notes.put_notes_by_id(
        _id="64298e2b6747aa02118d3c23",
        title="Changed_title",
        description="Changed_description",
        status="true",
        category="Personal",
        expected_status_code=404,
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_put_notes_without_note_id(created_notes):
    response = created_notes.put_notes_by_id(
        title="Changed_title",
        description="Changed_description",
        status="true",
        category="Personal",
        expected_status_code=400,
    )
    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_put_notes_without_description(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.put_notes_by_id(
        _id=id_notes,
        title="Changed_title",
        status="true",
        category="Personal",
        expected_status_code=400,
    )
    assert response_got_note["success"] is False
    assert (
        response_got_note["message"]
        == "Description must be between 4 and 1000 characters"
    )


def test_put_notes_without_title(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.put_notes_by_id(
        _id=id_notes,
        description="Changed_description",
        status="true",
        category="Personal",
        expected_status_code=400,
    )
    assert response_got_note["success"] is False
    assert response_got_note["message"] == "Title must be between 4 and 100 characters"


def test_put_notes_without_status(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.put_notes_by_id(
        _id=id_notes,
        title="Changed_title",
        description="Changed_description",
        category="Personal",
        expected_status_code=400,
    )
    assert response_got_note["success"] is False
    assert response_got_note["message"] == "Note completed status must be boolean"


def test_put_notes_without_category(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.put_notes_by_id(
        _id=id_notes,
        title="Changed_title",
        description="Changed_description",
        status="true",
        expected_status_code=400,
    )
    assert response_got_note["success"] is False
    assert (
        response_got_note["message"]
        == "Category must be one of the categories: Home, Work, Personal"
    )


def test_patch_notes_by_id(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.patch_notes_by_id(_id=id_notes, status="false")
    assert response_got_note["success"] is True
    assert response_got_note["message"] == "Note successfully Updated"
    assert response_got_note["data"]["completed"] is False


def test_patch_notes_by_nonexistent_id(created_notes):
    response = created_notes.patch_notes_by_id(
        _id="64298e2b6747aa02118d3c23", status="false", expected_status_code=404
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_patch_notes_without_note_id(created_notes):
    response = created_notes.patch_notes_by_id(status="false", expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_v_notes_without_status(created_notes):
    response = created_notes.get_notes()
    id_notes = response["data"][1]["id"]
    response_got_note = created_notes.patch_notes_by_id(
        _id=id_notes, expected_status_code=400
    )
    assert response_got_note["success"] is False
    assert response_got_note["message"] == "Note completed status must be boolean"


def test_delete_notes_by_id(created_notes):
    response = created_notes.get_notes()
    first_id_note = response["data"][0]["id"]
    response_got_note = created_notes.delete_notes_by_id(first_id_note)
    assert response_got_note["success"] is True
    assert response_got_note["message"] == "Note successfully deleted"
    response_second_got_note = created_notes.get_notes()
    second_id_note = response_second_got_note["data"][0]["id"]
    assert first_id_note != second_id_note


def test_delete_notes_by_nonexistent_id(created_notes):
    response = created_notes.delete_notes_by_id(
        _id="64298e2b6747aa02118d3c23", expected_status_code=404
    )
    assert response["success"] is False
    assert (
        response["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_delete_notes_without_id(created_notes):
    response = created_notes.delete_notes_by_id(expected_status_code=400)
    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_delete_notes_by_id_with_invalid_token(created_notes):
    current_token = created_notes._token
    response = created_notes.get_notes()
    id_note = response["data"][0]["id"]
    created_notes._token = (
        "fdf374ed410e468a9e9349def4d72228caf45b87a7f3430cadba3b3cb6d660e9"
    )
    response = created_notes.delete_notes_by_id(id_note, expected_status_code=401)
    assert response["success"] is False
    assert (
        response["message"]
        == "Access token is not valid or has expired, you will need to login"
    )
    created_notes._token = current_token
