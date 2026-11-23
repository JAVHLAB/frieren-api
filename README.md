# Frieren API

A RESTful API built with **FastAPI** and containerized with **Docker** and **Docker Compose**.

## Tech Stack
* **Framework:** FastAPI (Python)
* **Database / ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Containerization:** Docker & Docker Compose

## Project Structure
```text
frieren_api/
├── app/
│   ├── routers/       # API route handlers
│   ├── __init__.py
│   ├── database.py    # Database connection and session setup
│   ├── main.py        # FastAPI application entry point
│   ├── models.py      # ORM database models
│   └── schemas.py     # Pydantic schemas for request/response validation
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Getting Started

### Prerequisites
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Running with Docker
1. Clone the repository:
   ```bash
   git clone [https://github.com/JAVHLAB/frieren_api.git](https://github.com/TU_USUARIO/frieren_api.git)
   cd frieren_api
   ```

2. Build and start the containers:
   ```bash
   docker compose up --build
   ```

3. Access the interactive API documentation (Swagger UI):
   * Open `http://localhost:8000/docs` in your browser.

### Stopping the containers
```bash
docker compose down
```