# Railway Management System

This is a railway management system designed to handle user registrations, train management, seat bookings, and more. Built using Django and PostgreSQL, it includes features like real-time seat availability and role-based access control.

## Features

- User Registration and Login
- Train Management (Admin Only)
- Seat Availability Checking
- Seat Booking with Concurrency Handling
- Role-Based Access Control
- API Key Protection for Admin Endpoints

## Tech Stack

- Backend: Django, Django Rest Framework
- Database: PostgreSQL
- Authentication: Token-based

## Requirements

- Python 3.8
- PostgreSQL
- Django 3.2 or higher

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gaurav4200/railway_management.git
``````

### 2. Set Up Virtual Environment
Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### 4. Configure the Database
Update the DATABASES setting in railway_management/settings.py with your PostgreSQL credentials:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway_management',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
Run the database migrations to set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Create a Superuser
Create a superuser to access the admin site:
```bash
python manage.py createsuperuser
```
### 7. Run the Development Server
Start the Django development server:
```
python manage.py runserver
```
### 8. Access the Application
Open your web browser and go to http://127.0.0.1:8000/ to access the application