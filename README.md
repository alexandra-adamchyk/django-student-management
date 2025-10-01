# Django Students Basic

First step in Django: simple student management app.  
Includes a form for adding students and a page for listing them.

## Features
- Create new students (first name, last name, nickname)
- List all students
- Navigation link to add new student

## Tech Stack
- Python 3, Django
- SQLite (default)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://localhost:8000/students/
