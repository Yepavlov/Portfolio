def test_get_health_check(notes_rest_client):
    response = notes_rest_client.get_health_check()
    assert response["success"] is True
