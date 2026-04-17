# FastAPI Task Manager

## Project Overview
This is a production-ready Task Manager Web Application built using FastAPI for the backend and Vanilla HTML/JS for the frontend. It features secure JWT authentication, a responsive user interface, and complete test coverage.

## Tech Stack
- **Backend:** FastAPI, SQLAlchemy, Pydantic v2, Python-jose
- **Database:** SQLite (default)
- **Frontend:** Vanilla HTML, CSS, JavaScript (No frameworks)
- **Deployment:** Render (via render.yaml or Dockerfile)
- **Testing:** pytest, pytest-asyncio

## Folder Structure
```
task-manager/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── config.py
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       └── tasks.py
├── frontend/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

## Local Setup Instructions

1. **Clone repo**
   ```bash
   git clone <repository-url>
   cd task-manager
   ```

2. **Create venv**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Copy `.env.example` to `.env` and fill values:
   ```bash
   cp .env.example .env
   ```

5. **Run server**
   ```bash
   uvicorn backend.main:app --reload
   ```

6. **Open /docs**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger API documentation.
   Visit the frontend by opening `frontend/index.html` directly in your browser.

## Environment Variables
| Variable | Description | Default / Example |
| -------- | ----------- | ----------------- |
| `DATABASE_URL` | The SQLAlchemy connection string | `sqlite:///./sql_app.db` |
| `SECRET_KEY` | Secret key for JWT hashing | `your-secret-key...` |
| `ALGORITHM` | The JWT signing algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token validity duration | `30` |

## Testing
To run the automated tests, simply run:
```bash
pytest tests/
```

## Render Deployment Instructions
1. Push your repository to GitHub.
2. Sign in to Render (https://render.com).
3. Click "New" and select "Blueprint".
4. Connect your GitHub repository.
5. Render will automatically apply the configuration from `render.yaml` and deploy the application.
6. The frontend needs point to the deployed Backend API in the JS code (update `const API` variable inside `frontend/index.html`).

## Live Demo!!
👉 https://task-manager-web-application-ixb7.onrender.com/

## API Endpoints

| Method | Path | Auth Required | Description |
| ------ | ---- | ------------- | ----------- |
| POST | `/register` | No | Register a new user |
| POST | `/login` | No | Login and get JWT token |
| POST | `/tasks` | Yes | Create a new task |
| GET | `/tasks` | Yes | Get all tasks (supports filtering, pagination) |
| GET | `/tasks/{id}` | Yes | Get a specific task |
| PUT | `/tasks/{id}` | Yes | Update a task (e.g., mark complete) |
| DELETE | `/tasks/{id}` | Yes | Delete a task |
