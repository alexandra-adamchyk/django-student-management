# Django ORM & CRUD — Lecture Notes

These are my personal notes from lessons while building the **Django Student Management** project.

---

## Tuesday Sept. 16 — Models & ORM (Part 1)

**Goals:**
- Understand what ORM (Object Relational Mapping) is and the problems it solves.
- Know the pros and cons of ORM.
- Be able to define Django models and sync them with PostgreSQL.
- Run migrations and see generated SQL with `sqlmigrate`.
- Write basic ORM queries.
- Convert existing DB tables into Django models using `inspectdb`.

**Technology breakdown:**
- Python, SQL, HTML, CSS, JavaScript, Django
- Context switching between different languages/frameworks
- ORM = bridge between Python classes and relational database tables

**Challenge:**
- Create a `students` application.
- Define a `Student` model with `first_name`, `last_name`, `nickname`.
- Add the app to `INSTALLED_APPS`.
- Run `makemigrations` and `migrate`.

**Commands:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

In the shell:
```python
from students.models import Student
Student.objects.create(first_name="John", last_name="Doe", nickname="JD")
```

Check with SQL:
```sql
SELECT * FROM students_student;
\dt
```

**Summary:**
- Always check spelling.
- Add new apps to `INSTALLED_APPS`.
- After changing `models.py`, run `makemigrations` + `migrate`.
- Relax, learning takes time — practice!

---

## Wednesday Sept. 17 — ORM Manager & Queries

**Learning Goals:**
- Identify and use the Django ORM model manager.
- Create database records using the Manager.
- Query with the Manager and understand QuerySets.
- Use `.filter()` for conditional queries.
- Update and delete records.
- Migration-related task: add new fields to a table.

---

### Creating Records (INSERT)
**Method 1**
```python
student1 = Student.objects.create(**kwargs)
```

**Method 2**
```python
student2 = Student(**kwargs)  # object created but no ID yet
student2.save()               # new ID is generated
```

**Bulk creation**
```python
Student.objects.bulk_create([
    Student(**kwargs),
    Student(**kwargs),
])
```

---

### QuerySets
- Collection of database records
- Lazy evaluation: query executes only when needed
- Can be chained (`.filter().exclude().order_by()`)

Examples:
```python
Student.objects.all()
list(Student.objects.all())
students = Student.objects.all()
students[1:10]
students.first()
students.last()
```

---

### Updating Records (UPDATE)
**Method 1**
```python
student = Student.objects.get(id=1)
student.first_name = "Anna"
student.save()
```

**Method 2**
```python
Student.objects.filter(first_name="William").update(last_name="Bah bah")
```

---

### Deleting Records (DELETE)
```python
Student.objects.get(id=2).delete()
Student.objects.filter(first_name="Joe").delete()
Student.objects.all().delete()
```

---

### Hints
- Use primary keys (id, passport number, SKU, etc.) for safer queries.
- Always make migrations after changing models.
- Managers and QuerySets = Python way of writing SQL.
