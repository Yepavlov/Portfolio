Notes REST API Testing Framework
This Python project provides a testing framework for conducting API tests on the Notes REST API service. It is built on top of the BaseRestClient class, offering a set of methods to interact with various endpoints of the API. The API endpoints include user management, profile updates, password operations, and interactions with notes.

Setup
To use this framework, you need to have Python 3.x installed on your machine. Install the required dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
Configuration
The base URL for the Notes REST API is set to https://practice.expandtesting.com/notes/api/. You can modify the BASE_URL attribute in the NotesRestClient class if the API endpoint changes.

Usage
Basic Usage
Initialize the NotesRestClient:

python
Copy code
from rest_api_testing_framework_notes_swagger.rest.base_rest_client import NotesRestClient

notes_rest_client = NotesRestClient()
User Registration and Login:

python
Copy code
# Register a new user
response_register = notes_rest_client.post_users_register("username", "email@example.com", "password")

# Login with the registered user
response_login = notes_rest_client.post_users_login("email@example.com", "password")
User Profile and Update:

python
Copy code
# Get user profile
response_profile = notes_rest_client.get_users_profile()

# Update user profile
response_update_profile = notes_rest_client.patch_users_profile("NewUsername", "123456789", "NewCompany")
Notes Operations
Create a New Note:

python
Copy code
response_create_note = notes_rest_client.post_notes("Note Title", "Note Description", "Note Category")
Get List of Notes:

python
Copy code
response_get_notes = notes_rest_client.get_notes()
Get a Specific Note by ID:

python
Copy code
note_id = "123"
response_get_note_by_id = notes_rest_client.get_notes_by_id(note_id)
Update a Note by ID:

python
Copy code
note_id = "123"
response_update_note = notes_rest_client.put_notes_by_id(note_id, "New Title", "New Description", "completed", "New Category")
Delete a Note by ID:

python
Copy code
note_id = "123"
response_delete_note = notes_rest_client.delete_notes_by_id(note_id)
User Authentication and Password Operations
Forgot Password:

python
Copy code
user_email = "email@example.com"
response_forgot_password = notes_rest_client.post_users_forgot_password(user_email)
Change Password:

python
Copy code
response_change_password = notes_rest_client.post_users_change_password("current_password", "new_password")
Logout:

python
Copy code
response_logout = notes_rest_client.delete_users_logout()
Delete User Account:

python
Copy code
response_delete_account = notes_rest_client.delete_users_delete_account()
Running Tests
The project includes a set of tests that demonstrate the usage of the framework. You can run the tests using a testing framework of your choice.

For example, to run the tests using pytest, use the following command:

bash
Copy code
pytest test_notes_rest_client.py
Contribution
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
