# Django REST API Project

This project is a Django-based REST API application that provides functionality for user registration, login, creating posts, and liking posts. The API uses JWT authentication for secure access.

## Features

* User registration and login with JWT authentication.
* Create, update, delete, and view posts.
* Like and unlike posts.
* Permissions: Users can only update or delete their own posts.

## Technologies Used

* Python 3.x
* Django 5.1.3
* Django REST Framework
* Django REST Framework Simple JWT
* SQLite (default database)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

* **Register**: `POST /api/register/`

  * Request Body: `username`, `password`, `email`
  * Response: Registration status

* **Login**: `POST /api/login/`

  * Request Body: `username`, `password`
  * Response: JWT tokens (`access` and `refresh`)

### Posts

* **List/Create Posts**: `GET/POST /api/posts/`
* **Retrieve/Update/Delete Post**: `GET/PUT/DELETE /api/posts/{id}/`
* **Like/Unlike Post**: `POST /api/like/{id}/`

> Note: Only the author of a post can update or delete it.

## Models

* **User**: Default Django user model
* **Post**:

  * `title`: CharField
  * `content`: TextField
  * `author`: ForeignKey to User
  * `like`: ManyToManyField to User

## Usage

1. Register a new user via `/api/register/`
2. Login to receive JWT tokens via `/api/login/`
3. Use the `Authorization: Bearer <access_token>` header to access protected endpoints.
4. Create, update, delete, and like posts using the API endpoints.

## Requirements

The `requirements.txt` file should include:

```
django>=5.1.3
djangorestframework
djangorestframework-simplejwt
```

## Admin Panel

* Access via `/admin/` after creating a superuser.
* Manage users and posts through the admin interface.

## License

This project is open-source and available for modification and distribution.
