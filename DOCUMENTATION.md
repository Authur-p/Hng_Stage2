# Django CRUD REST API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [API Endpoints](#api-endpoints)
    - [GET /api/users/](#get-apiusers)
    - [GET /api/users/{id}/](#get-apiusersid)
    - [POST /api/users/](#post-apiusers)
    - [PUT /api/users/{id}/](#put-apiusersid)
    - [PATCH /api/users/{id}/](#patch-apiusersid)
    - [DELETE /api/users/{id}/](#delete-apiusersid)
3. [Known Limitation](#known-limitation)
4. [Deployment](#deployment)

## Introduction

This document provides detailed documentation for the Django CRUD REST API. The API allows you to manage user data, including creating, reading, updating, and deleting user records. It follows RESTful principles and provides secure authentication and authorization.

## API Endpoints

### GET /api/user/

Retrieve a list of all users.

**Response:**

- Status Code: 200 OK
- Content-Type: application/json

```json
[
  {
    "id": 1,
    "name": "user1",
    "email": "user1@example.com",
    "age": ""32
  },
  {
    "id": 2,
    "name": "user2",
    "email": "user2@example.com",
    "age": "56"
  }
]
```

### POST /api/user/

Create a new user.
Content-Type: application/json

```json
{
    "name": "user3",
    "email": "user1@example.com",
    "age": "43"
  }
```

**Response:**

- Status Code: 201 Created
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3",
    "email": "user3@example.com"
    "age": "43"
  }
```

### GET /api/user/{name}

Get a user through name.

**Response:**

- Status Code: 200 Ok
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3",
    "email": "user1@example.com",
    "age": "43"
  }
```

### PUT /api/user/{name}

Update an existing user.
Content-Type: application/json

```json
{
    "name": "user3-updated",
    "email": "user1@example.com",
    "age": "43"
  }
```

**Response:**

- Status Code: 200 Ok
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3-updated",
    "email": "user3@example.com"
    "age": "43"
  }
```

### DDELETE /api/user/{name}

Delete a user.

**Response:**

- Status Code: 204 No Content

## Known Limitation

- The API contained, does not make user of any authentication, permission or throttling.

## Deployment

1. Push project directory to github:
```bash
git init
git add .
git commit -m "init"
git remote add origin git@github.com:user-name/myprojectname.git
git push
```

2. Go to [Pythonanywhere](#pythonanywhere.com)



