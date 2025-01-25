# Phonebook API

## Description
This project provides a simple API for managing a phone book, allowing users to add, view, search, update, and delete contacts. Each contact contains information like name, phone number, and email. The project is built using **Django** and **Django REST Framework**, and the API endpoints are tested using **Postman**.


## Features
- **Add Contact**: Add new contacts with name, phone number, and email.
- **View All Contacts**: Retrieve all contacts in the phone book.
- **Search Contact**: Search for a contact by name or phone number.
- **Update Contact**: Modify contact information.
- **Delete Contact**: Remove a contact from the phone book.
- **Validation**: Email and phone number are validated for uniqueness and correct format.

## Tech Stack

- **Backend**: Django (with Django REST Framework)
- **Database**: SQLite (default) or you can configure any other DB (e.g., PostgreSQL, MySQL)
- **PDF Generation**: WeasyPrint for PDF export functionality
- **Postman**: Used for testing and interacting with the API endpoints.

## Installation

### Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/Ahmad-Jaber0/PhoneBook.git
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional, to access the admin interface):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

7. Visit the API documentation at `http://127.0.0.1:8000/` to see the available endpoints.

## API Endpoints

### 1. Add a New Contact

- **URL**: `/api/contacts/`
- **Method**: `POST`
- **Request Body**:

    ```json
    {
      "name": "Ahmad",
      "phone": "123456789",
      "email": "jojo@example.com"
    }
    ```

- **Response**: 201 Created

---

### 2. Get All Contacts

- **URL**: `/api/contacts/`
- **Method**: `GET`
- **Response**:

    ```json
    [
      {
        "id": 1,
        "name": "Ahmad",
        "phone": "123456789",
        "email": "jojo@example.com"
      },
      {
        "id": 2,
        "name": "Jane",
        "phone": "987654321",
        "email": "jane@example.com"
      }
    ]
    ```

---

### 3. Get Contact by ID

- **URL**: `/api/contacts/{id}/`
- **Method**: `GET`
- **Response**:

    ```json
    {
      "id": 1,
      "name": "Ahmad",
      "phone": "123456789",
      "email": "jojo@example.com"
    }
    ```

---

### 4. Update Contact

- **URL**: `/api/contacts/{id}/`
- **Method**: `PUT`
- **Request Body**:

    ```json
    {
      "name": "Ahmad",
      "phone": "111222333",
      "email": "jojo@example.com"
    }
    ```

- **Response**: 200 OK

---

### 5. Delete Contact

- **URL**: `/api/contacts/{id}/`
- **Method**: `DELETE`
- **Response**: 204 No Content

---

### 6. Export Contacts to PDF

- **URL**: `/api/contacts/export/`
- **Method**: `GET`
- **Response**: PDF file download containing all contacts.
