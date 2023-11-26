# Django Blog API

This is a simple Django project developed to create a basic blog API using Django REST Framework (DRF).

## Features

- Manages Authors, Posts, and Comments.
- Utilizes Django's models for data representation.
- Implements Django REST Framework for API endpoints.
- Includes serializers for handling data conversion.
- Implements data validation using serializers.

## Installation

### Prerequisites

- Python 3.10
- Django
- Django REST Framework

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/hmabubakar313/exp_django.git

1. Navigate to the project directory:
   * cd exp_django
2. Create a virtual environment:
   * python3 -m venv venv
3. Activate the virtual environment:
  * On Windows:
       venv\Scripts\activate
4. Install dependencies:
  * pip install -r requirements.txt
5. Perform database migrations:
   * python manage.py migrate
**Usage**
1. Run the development server:
   * python manage.py runserver
2. Access the API:
Open your web browser and go to: http://127.0.0.1:8000/

### Available Endpoints

- **Authors:** `/authors/`
  - Methods: GET (List), POST (Create)
- **Posts:** `/posts/`
  - Methods: GET (List), POST (Create)
- **Comments:** `/comments/`
  - Methods: GET (List), POST (Create)

### API Endpoints

- **Authors:** `/authors/`
  - Methods: GET (List), POST (Create)
- **Posts:** `/posts/`
  - Methods: GET (List), POST (Create)
- **Comments:** `/comments/`
  - Methods: GET (List), POST (Create)


