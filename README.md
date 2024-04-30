# drf_crud

DRF CRUD Operations

This project is a Django application built with Django Rest Framework (DRF) to perform CRUD (Create, Read, Update, Delete) operations on a database. It provides a RESTful API for managing family records stored in the database.
Features

    Create, Read, Update, and Delete family records via RESTful API endpoints.
    Secure authentication and authorization mechanisms for accessing API endpoints.
    Utilizes Django ORM for efficient database interactions.
    Comprehensive testing ensures the reliability and functionality of CRUD operations.
    Clean and maintainable codebase following best practices in Django development.

Getting Started

To run this project locally, follow these steps:

    Clone the repository to your local machine:

    bash

git clone https://github.com/YaminLamBappi/drf_crud.git

Navigate to the project directory:

bash

cd drf_crud

Install the required dependencies:

pip install -r requirements.txt

Migrate the database to apply migrations:

python manage.py migrate

Run the development server:

    python manage.py runserver

    Access the API endpoints in your browser or through a tool like Postman:
        List all families: http://127.0.0.1:8000/crud/familyapi/ (GET)
        Create a new family: http://127.0.0.1:8000/crud/familyapi/ (POST)
        Retrieve, update, or delete a family by ID: http://127.0.0.1:8000/crud/familyapi/{id}/ (GET, PUT, DELETE)

Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
