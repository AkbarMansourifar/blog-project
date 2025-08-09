# Blog Project API

This is a RESTful API for managing blog posts, built with Django and Django REST Framework.

## Features

- User registration and JWT authentication
- Create, read, update, and delete blog posts
- Permission control: only authenticated users can create/update/delete their own posts
- Public read access to blog posts

## Requirements

- Python 3.8+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AkbarMansourifar/blog-project.git
   cd blog-project
   ```

2. Create and activate a virtual environment:

   - On Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Register a new user via `/api/auth/register/` (POST)
- Obtain JWT token via `/api/auth/login/` (POST)
- Refresh JWT token via `/api/auth/refresh/` (POST)
- Access blog posts API at `/api/posts/`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
