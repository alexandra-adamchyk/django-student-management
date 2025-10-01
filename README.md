# Django Student Management (CRUD Basics)

A simple Django project to demonstrate the basics of Django ORM and CRUD operations.  
This project was built as part of a learning exercise.

## Features
- Define a `Student` model with `first_name`, `last_name`, and `nickname`.
- Create new students via form submissions.
- Display a list of all students.
- Perform basic ORM operations (Create, Read, Update, Delete).
- Explore database migrations and working with PostgreSQL.

## Tech Stack
- Python 3
- Django (see `requirements.txt`)
- SQLite (default) / PostgreSQL (optional)

## Learning Goals
- Understand Django ORM and the role of the Model Manager.
- Create records using `.create()` and `.save()`.
- Query with `.all()`, `.filter()`, `.get()` and understand QuerySets.
- Update and delete records.
- Perform migrations and schema changes.

## Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/django-student-management.git
cd django-student-management
pip install -r requirements.txt
```

Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:
```bash
python manage.py runserver
```

Open [http://localhost:8000/students/](http://localhost:8000/students/) in your browser.

## Example ORM Queries
Inside the Django shell:
```python
from students.models import Student

# Create
student = Student.objects.create(first_name="Anna", last_name="Smith", nickname="Annie")

# Read
students = Student.objects.all()
Student.objects.filter(first_name="Anna")

# Update
student = Student.objects.get(id=1)
student.nickname = "Ann"
student.save()

# Delete
Student.objects.filter(first_name="Anna").delete()
```

## Author
Alexandra Adamchyk
