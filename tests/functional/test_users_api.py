from fastapi.testclient import TestClient

def sample_user_json():
    return {
        "corporate_name": "Test",
        "phone": "123456789",
        "address": "Test address",
        "registration_date": "01/01/2021",
        "declared_revenue": 1000.00,
        "bank_details": [
            {
                "bank": "Test Bank",
                "agency": "1234",
                "account": "123456",
            }
        ],
    }

def sample_user_response():
    return {
        "corporate_name": "Test",
        "phone": "123456789",
        "address": "Test address",
        "registration_date": "2021-01-01",
        "declared_revenue": 1000.00,
        "bank_details": [
            {
                "bank": "Test Bank",
                "agency": "1234",
                "account": "123456",
            }
        ],
    }

def test_list_users(client: TestClient):
    # Get list of users
    response = client.get("/users/")

    # Create expected response
    expected_response = []

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_list_users_with_one_user(client: TestClient):
    # Add user to database
    client.post("/users/", json=sample_user_json())

    # Get list of users
    response = client.get("/users/")

    # Create expected response
    expected_response = [sample_user_response()]

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_user_insertion_without_bank_details(client: TestClient):
    # Create user without bank details
    user_json = sample_user_json()
    user_json["bank_details"] = []

    # Insert user
    client.post("/users/", json=user_json)

    # Create expected response
    expected_response = sample_user_response()
    expected_response["bank_details"] = []

    # Get user
    response = client.get("/users/1")

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_user_insertion_with_bank_details(client: TestClient):
    # Insert user
    client.post("/users/", json=sample_user_json())

    # Create expected response
    expected_response = sample_user_response()

    # Get user
    response = client.get("/users/1")

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_user_insertion_with_invalid_registration_date(client: TestClient):
    # Create user with invalid registration date
    user_json = sample_user_json()
    user_json["registration_date"] = "0101/2021" # Missing / between day and month

    # Insert user
    response = client.post("/users/", json=user_json)

    # Check if response is error 422
    assert response.status_code == 422

def test_user_insertion_with_invalid_bank_details(client: TestClient):
    # Create user with invalid bank details
    user_json = sample_user_json()
    user_json["bank_details"][0]["agency"] = "acbd" # Agency must be only numbers

    # Insert user
    response = client.post("/users/", json=user_json)

    # Check if response is error 422
    assert response.status_code == 422

def test_get_user_by_id(client: TestClient):
    # Add user to database
    client.post("/users/", json=sample_user_json())

    # Get user
    response = client.get("/users/1")

    # Create expected response
    expected_response = sample_user_response()

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_get_user_by_invalid_id(client: TestClient):
    # Try to get
    response = client.get("/users/1")

    # Check if response is error 404
    assert response.status_code == 404

def test_update_user_by_id(client: TestClient):
    # Add user to database
    client.post("/users/", json=sample_user_json())

    # Update user
    user_json = sample_user_json()
    user_json["corporate_name"] = "Updated Test"
    client.put("/users/1", json=user_json)

    # Get user
    response = client.get("/users/1")

    # Create expected response
    user_response = sample_user_response()
    user_response["corporate_name"] = "Updated Test"

    # Assert response
    assert response.status_code == 200
    assert response.json() == user_response

def test_update_user_by_invalid_id(client: TestClient):
    # Try to update user
    response = client.put("/users/1", json=sample_user_json())

    # Check if response is error 404
    assert response.status_code == 404

def test_delete_user_by_id(client: TestClient):
    # Add user to database
    client.post("/users/", json=sample_user_json())

    # Delete user
    client.delete("/users/1")

    # Get list of users
    response = client.get("/users/")

    # Create expected response
    expected_response = []

    # Assert response
    assert response.status_code == 200
    assert response.json() == expected_response

def test_delete_user_by_invalid_id(client: TestClient):
    # Try to delete user
    reponse = client.delete("/users/1")

    # Check if response is error 422
    assert reponse.status_code == 404