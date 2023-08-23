def test_create_notes(authenticated_notes_service):
    response = authenticated_notes_service.post_notes("Test", "Testing notes", "Work")
    assert response["data"]["title"] == "Test"
    assert response["data"]["description"] == "Testing notes"
    assert response["data"]["category"] == "Work"


def test_get_all_notes(prepared_notes):
    response = prepared_notes.get_all_notes()
    assert response["message"] == "Notes successfully retrieved"
    assert response["data"][0]["title"] == "Test2"
    assert response["data"][0]["description"] == "Testing notes2"
    assert response["data"][0]["category"] == "Home"
    assert response["data"][1]["title"] == "Test"
    assert response["data"][1]["description"] == "Testing notes"
    assert response["data"][1]["category"] == "Work"


def test_get_note_by_id(prepared_notes):
    response = prepared_notes.get_all_notes()
    _id = response["data"][1]["id"]
    response_by_id = prepared_notes.get_notes_by_id(_id)
    assert response_by_id["data"]["title"] == "Test"
    assert response_by_id["data"]["description"] == "Testing notes"
    assert response_by_id["data"]["category"] == "Work"


def test_get_note_by_incorrect_id(prepared_notes):
    response_by_id = prepared_notes.get_notes_by_id(
        "64298e2b6747aa02118d3c23", expected_status_code=404
    )
    assert response_by_id["status"] == 404
    assert (
        response_by_id["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_update_an_existing_note(prepared_notes):
    response = prepared_notes.get_all_notes()
    _id = response["data"][0]["id"]
    response_by_id = prepared_notes.put_notes_by_id(
        _id, "Update_note_title", "Update_note_description", "true", "Personal"
    )
    assert response_by_id["data"]["title"] == "Update_note_title"
    assert response_by_id["data"]["description"] == "Update_note_description"
    assert response_by_id["data"]["completed"] is True
    assert response_by_id["data"]["category"] == "Personal"


def test_update_an_nonexistent_id_note(prepared_notes):
    response_by_id = prepared_notes.put_notes_by_id(
        "64298e2b6747aa02118d3c23",
        "Update_note_title",
        "Update_note_description",
        "true",
        "Personal",
        expected_status_code=404,
    )
    assert response_by_id["status"] == 404
    assert (
        response_by_id["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_update_the_completed_attribute(prepared_notes):
    response = prepared_notes.get_all_notes()
    _id = response["data"][0]["id"]
    response_by_id = prepared_notes.patch_notes_by_id(_id, "false")
    assert response_by_id["data"]["completed"] is False


def test_update_the_completed_attribute_by_incorrect_id(prepared_notes):
    response_by_id = prepared_notes.patch_notes_by_id(
        "64298e2b6747aa02118d3c23", "false", expected_status_code=404
    )
    assert response_by_id["status"] == 404
    assert (
        response_by_id["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )


def test_delete_a_note_by_id(prepared_notes):
    response = prepared_notes.get_all_notes()
    _id = response["data"][0]["id"]
    response_by_id = prepared_notes.delete_notes_by_id(_id)
    assert response_by_id["message"] == "Note successfully deleted"


def test_delete_a_note_by_incorrect_id(prepared_notes):
    response_by_id = prepared_notes.delete_notes_by_id(
        "64298e2b6747aa02118d3c23", expected_status_code=404
    )
    assert response_by_id["status"] == 404
    assert (
        response_by_id["message"]
        == "No note was found with the provided ID, Maybe it was deleted"
    )
