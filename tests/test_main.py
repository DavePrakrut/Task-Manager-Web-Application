def test_register_new_user(client):
    response = client.post(
        "/register",
        json={"username": "newuser", "email": "newuser@test.com", "password": "password123"}
    )
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"

def test_duplicate_user_registration(client, auth_fixture):
    # auth_fixture already creates 'testuser'
    response = client.post(
        "/register",
        json={"username": "testuser", "email": "test@test.com", "password": "password123"}
    )
    assert response.status_code == 400

def test_login_correct_credentials(client, auth_fixture):
    # 'testuser' existing
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_credentials(client, auth_fixture):
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_create_task(client, auth_fixture):
    headers = auth_fixture
    response = client.post(
        "/tasks",
        headers=headers,
        json={"title": "My Test Task", "description": "Test Desc"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My Test Task"
    assert data["completed"] is False

def test_get_tasks_list_pagination(client, auth_fixture):
    headers = auth_fixture
    
    for i in range(15):
        client.post("/tasks", headers=headers, json={"title": f"Task {i}"})
        
    response1 = client.get("/tasks?skip=0&limit=10", headers=headers)
    assert response1.status_code == 200
    assert len(response1.json()) == 10
    
    response2 = client.get("/tasks?skip=10&limit=10", headers=headers)
    assert response2.status_code == 200
    assert len(response2.json()) == 5

def test_mark_task_completed(client, auth_fixture):
    headers = auth_fixture
    task = client.post("/tasks", headers=headers, json={"title": "To be completed"}).json()
    task_id = task["id"]
    
    response = client.put(f"/tasks/{task_id}", headers=headers, json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True
    
def test_delete_task(client, auth_fixture):
    headers = auth_fixture
    task = client.post("/tasks", headers=headers, json={"title": "To be deleted"}).json()
    task_id = task["id"]
    
    response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 204
    
    get_response = client.get(f"/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 404
