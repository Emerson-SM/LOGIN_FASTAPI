# User Management System

A lightweight web application built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2** that provides user registration, authentication, and management features.

The project was developed to practice backend development concepts, database integration, API design, and server-side rendering using modern Python technologies.

---

## Features

* User registration
* User authentication (login)
* User profile page
* User management CRUD operations
* SQLite database integration
* SQLAlchemy ORM models
* Server-side rendered HTML pages with Jinja2
* FastAPI automatic API documentation
* Form handling and validation

---

## Technologies Used

### Backend

* Python 3
* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* HTML5
* Bootstrap
* Jinja2 Templates

### Development Tools

* Uvicorn
* Visual Studio Code
* Git & GitHub

---

## Project Structure

```text
project/
│
├── app/
│   ├── database/
│   │   ├── db.py
│   │   ├── models/
│   │   └── schemas/
│   │
│   ├── routes/
│   │   ├── user_routes.py
│   │   └── db_routes.py
│   │
│   ├── view/
│   │   ├── index.html
│   │   ├── signup.html
│   │   └── user.html
│   │
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Learning Objectives

This project was created to strengthen knowledge in:

* REST API development
* Database modeling
* ORM usage with SQLAlchemy
* FastAPI architecture
* HTML form processing
* User authentication concepts
* Backend project organization

---

## Future Improvements

* Password hashing
* JWT authentication
* Session management
* Role-based authorization
* Improved form validation
* User profile editing
* PostgreSQL support
* Docker deployment

---

## License

This project is intended for educational and portfolio purposes.
