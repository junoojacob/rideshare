# Ride-Sharing API Project

A basic ride-sharing API built with Django and Django REST Framework. This project provides endpoints for user registration, creating and managing rides, and real-time status updates.

---

## Features

- User registration and token-based authentication (`/api/register/`, `/api/login/`).
- Full CRUD (Create, Read, Update, Delete) functionality for rides.
    * Custom action for riders to request a ride (`/api/rides/`)
    * Custom actions for drivers to accept rides (`/api/rides/{id}/accept/`).
    * Custom actions for viewing and updating ride status and location.(`/api/rides/{id}/`,`/api/rides/{id}/update-status/`)

## API Documentation

    * Automatically generated, interactive API documentation via Swagger UI. (`/api/schema/swagger-ui/`)
## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1.  Clone the repository:
    ```sh
    git clone (https://github.com/junoojacob/rideshare.git)
    ```
2.  Navigate into the project directory:
    ```sh
    cd your-repo-name
    ```
3.  Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  
    ```
4.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5.  Run database migrations:
    ```sh
    python manage.py migrate
    ```
6.  Start the development server:
    ```sh
    python manage.py runserver
    ```