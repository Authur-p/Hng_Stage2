# Django CRUD REST API

![Python](https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue)
![Django](https://img.shields.io/badge/Django-3.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A simple CRUD (Create, Read, Update, Delete) REST API built with Django for managing user data.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Testing](#testing)

## Features

- Create, read, update, and delete user records.
- RESTful API design for easy integration with front-end applications.
- Secure authentication and authorization.
- Detailed documentation of API endpoints.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.5 installed.
- Django 3.2 installed.
- [PostgreSQL](https://www.postgresql.org/) or another database system set up.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-crud-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Hng_Stage2
   ```
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the API at `http://127.0.0.1:8000/api/`

## API Endpoints

- **`GET /api/user`:** Retrieve a list of all users.
- **`GET /api/users/{name}`:** Retrieve details of a specific user, through the name.
- **`POST /api/user`:** Create a new user.
- **`PUT /api/user/{name}`:** Update an existing user.
- **`DELETE /api/user/{name}`:** Delete an existing user.

## Usage

### Create a new user

```http
POST /api/user
Content-Type: application/json

{
  "name": "newuser",
  "email": "newuser@example.com",
  "age": "25"
}
```
- Response:
  
```json
{
  "id": 1,
  "name": "newuser",
  "email": "newuser@example.com",
  "age": "25"
}
```

### List of all user

```http
GET /api/user
```

### Get a person by name

```http
GET /api/user/{name}
```

- Response:
  
```json
{
  "id": 1,
  "name": "newuser",
  "email": "newuser@example.com",
  "age": "25"
}
```

### Update an existing user

```http
PUT /api/user/{name}
{
  "name": "newuser-updated",
  "email": "newuser@example.com",
  "age": "25"
}
```

- Response:
  
```json
{
  "id": 1,
  "name": "newuser-updated",
  "email": "newuser@example.com",
  "age": "25"
}
```

### Delete an existing user

```http
DELETE /api/user/{name}
{
   "id": 1,
  "name": "newuser-updated",
  "email": "newuser@example.com",
  "age": "25"
}
```

- Response:
  
```http
204 No Content
```


## Error Handling

- If the provided ID does not exist, you will receive a `404 Not Found` response.
- If there is an internal server error, you will receive a `500 Internal Server Error` response.

## Testing

- To run test, djangorestframework, which was installed, provides a web based means of testing all endpoints.
- Also, using Postman is also a great way of testing all the endpoints.





   
