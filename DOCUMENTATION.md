# Django CRUD REST API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [API Endpoints](#api-endpoints)
    - [GET /api](#get-api)
    - [GET /api/{name}](#get-apiname)
    - [POST /api](#post-api)
    - [PUT /api/{name}](#put-apiname)
    - [PATCH /api/{name}](#patch-apiname)
    - [DELETE /api/{name}](#delete-apiname)
3. [Known Limitation](#known-limitation)
4. [Deployment](#deployment)

## Introduction

This document provides detailed documentation for the Django CRUD REST API. The API allows you to manage user data, including creating, reading, updating, and deleting user records.

Base URL
```bash
https://authur.pythonanywhere.com/api
```

## API Endpoints

### GET /api

Retrieve a list of all users.

**Response:**

- Status Code: 200 OK
- Content-Type: application/json

```json
[
  {
    "id": 1,
    "name": "user1"
  },
  {
    "id": 2,
    "name": "user2"
  }
]
```

### POST /api

Create a new user.
Content-Type: application/json

```json
  {
    "name": "user3"
  }
```

**Response:**

- Status Code: 201 Created
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3"
  }
```

### GET /api/{name}

Get a user through name.

**Response:**

- Status Code: 200 Ok
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3"
  }
```

### PUT /api/{name}

Update an existing user.
Content-Type: application/json

```json
  {
    "name": "user3-updated"
  }
```

**Response:**

- Status Code: 200 Ok
- Content-Type: application/json

```json
  {
    "id": 3,
    "name": "user3-updated"
  }
```

### DDELETE /api/{name}

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

2. Go to [Pythonanywhere](https://www.pythonanywhere.com/), create and account, then deploy it there



