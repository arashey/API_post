# Django REST API Project

This project is a simple Django REST API that allows users to register, log in, create posts, and like/unlike posts. The project uses Django REST Framework (DRF) and JWT for authentication.

## Features

* User registration and login with JWT authentication
* Create, update, and delete posts
* Like and unlike posts
* Only authors can edit or delete their own posts
* Retrieve all posts created by the authenticated user

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin panel):

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

## API Endpoints

### Auth

| Endpoint         | Method | Description                   |
| ---------------- | ------ | ----------------------------- |
| `/api/register/` | POST   | Register a new user           |
| `/api/login/`    | POST   | Log in and receive JWT tokens |

### Posts

| Endpoint           | Method | Description                           |
| ------------------ | ------ | ------------------------------------- |
| `/api/posts/`      | GET    | List all posts of authenticated user  |
| `/api/posts/`      | POST   | Create a new post (authenticated)     |
| `/api/posts/<id>/` | GET    | Retrieve a single post                |
| `/api/posts/<id>/` | PUT    | Update a post (author only)           |
| `/api/posts/<id>/` | DELETE | Delete a post (author only)           |
| `/api/like/<id>/`  | POST   | Like or unlike a post (authenticated) |

## JWT Authentication

* After login, you will receive a `refresh` token and an `access` token.
* Use the `access` token in the `Authorization` header for authenticated requests:

```
Authorization: Bearer <access_token>
```

## API Testing

You can test the API using tools like **Postman** or **cURL**:

1. **Register a new user**:

```bash
POST /api/register/
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

2. **Login**:

```bash
POST /api/login/
Content-Type: application/json

{
  "username": "testuser",
  "password": "password123"
}
```

Response:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

3. **Create a post**:

```bash
POST /api/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```

4. **Like a post**:

```bash
POST /api/like/<post_id>/
Authorization: Bearer <access_token>
```

Response:

```json
{
  "detail": "post liked"
}
```

5. **Unlike a post**:

```bash
POST /api/like/<post_id>/
Authorization: Bearer <access_token>
```

Response:

```json
{
  "detail": "post unliked"
}
```

## Requirements

* Python 3.10+
* Django 5.1.3
* Django REST Framework
* djangorestframework-simplejwt


## Admin Panel

* Access via `/admin/` after creating a superuser.
* Manage users and posts through the admin interface.

## License

This project is open-source and available for modification and distribution.
