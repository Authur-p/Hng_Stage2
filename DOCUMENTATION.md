# Django CRUD REST API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [API Endpoints](#api-endpoints)
    - [GET /api/users/](#get-apiusers)
    - [GET /api/users/{id}/](#get-apiusersid)
    - [POST /api/users/](#post-apiusers)
    - [PUT /api/users/{id}/](#put-apiusersid)
    - [PATCH /api/users/{id}/](#patch-apiusersid)
    - [DELETE /api/users/{id}/](#delete-apiusersid)
4. [Error Handling](#error-handling)
5. [Example Requests](#example-requests)

## Introduction

This document provides detailed documentation for the Django CRUD REST API. The API allows you to manage user data, including creating, reading, updating, and deleting user records. It follows RESTful principles and provides secure authentication and authorization.

## Authentication

Authentication for this API is based on Token Authentication. To access protected endpoints, clients must include an `Authorization` header with a valid token.

To obtain a token, send a `POST` request to `/api/token/` with valid credentials. The API will respond with a token that should be included in the `Authorization` header for subsequent requests.

## API Endpoints

### GET /api/users/

Retrieve a list of all users.

**Response:**

- Status Code: 200 OK
- Content-Type: application/json

```json
[
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com"
  },
  {
    "id": 2,
    "username": "user2",
    "email": "user2@example.com"
  }
]

