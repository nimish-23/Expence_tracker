# Expense Tracker API

A production-grade expense tracking REST API built with **FastAPI** and **PostgreSQL**, designed around clean architecture, secure authentication, and maintainable, testable code.

> ⚠️ **Status: In Development.** Core authentication is implemented. Expense/Category CRUD, testing, and containerization are in progress. See [Roadmap](#roadmap) below for current state.

---

## Features

### ✅ Implemented
- User registration and login
- JWT-based authentication
- Secure password hashing (`pwdlib`, Argon2)
- Protected routes via a reusable `get_current_user` dependency
- Environment-based configuration (`pydantic-settings`)
- PostgreSQL integration via SQLAlchemy 2.0
- Database migrations via Alembic

### 🚧 Planned
- Expense & Category CRUD with user-scoped ownership
- Pagination, filtering, sorting, and search on expense queries
- Automated test suite (pytest)
- Dockerized local development environment
- Role-based access control
- Rate limiting and security headers
- CI pipeline (GitHub Actions)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.0 |
| Migrations | Alembic |
| Auth | JWT (`python-jose`) |
| Password Hashing | `pwdlib` (Argon2) |
| Config | `pydantic-settings` |
| Server | Uvicorn |

---

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── config.py            # Environment-based settings
│   ├── database/
│   │   └── db.py            # Engine, session, and DB dependency
│   ├── models/
│   │   └── user.py          # SQLAlchemy models
│   ├── schemas/
│   │   ├── auth.py          # Request/response schemas for auth
│   │   └── user.py          # User-facing schemas
│   ├── routes/
│   │   └── auth.py          # Auth endpoints (register, login)
│   └── security/
│       ├── dependencies.py  # Auth dependency (current user)
│       ├── jwt.py           # Token creation/decoding
│       └── password.py      # Hashing and verification
├── alembic/                 # Migration environment and versions
└── requirements.txt
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL (running locally or accessible remotely)

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Expence_tracker.git
cd Expence_tracker/backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy the example file and fill in your own values:
```bash
cp .env.example .env
```

Required variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/expense_tracker
SECRET_KEY=your-secret-key
DEBUG=True
HOST=127.0.0.1
PORT=8000
```

### 5. Run database migrations
```bash
alembic upgrade head
```

### 6. Start the development server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

---

## API Overview

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/auth/register` | Register a new user | No |
| POST | `/auth/login` | Authenticate and receive a JWT | No |
| GET | `/auth/me` | Get the current authenticated user | Yes |

> Additional endpoints for expense and category management are in progress.

---

## Roadmap

This project follows a phased build plan focused on shipping a fully tested, containerized, and deployed backend rather than accumulating unused features.

- [x] **Phase 1** — Core FastAPI setup, PostgreSQL + SQLAlchemy, JWT authentication
- [ ] **Phase 2** — Expense/Category CRUD, ownership rules, initial test suite, Docker setup
- [ ] **Phase 3** — Pagination, filtering, sorting, search
- [ ] **Phase 4** — Query optimization, first deployment
- [ ] **Phase 5+** — Production patterns, RBAC, performance, background tasks, CI/CD

---

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Nimish Sinkar**
