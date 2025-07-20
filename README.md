# 🏫 School Management API (Django REST Framework)

This is a RESTful API for managing **schools, classrooms, teachers, and students** using Django REST Framework and `django-filter`. The API supports full CRUD operations, nested relationships, and filterable list endpoints.

---

## 📦 Technologies Used

- Python 3.10+
- Django 4.x
- Django REST Framework
- django-filter
- SQLite

---

## 📁 Data Models

### 🏫 School
- `name`: School name
- `short_name`: Abbreviation
- `address`: School address

### 🏫 Classroom
- `year`: Grade/Level
- `section`: Class section
- `school`: ForeignKey to School (`related_name='classrooms'`)

### 👨‍🏫 Teacher
- `first_name`, `last_name`
- `gender`: M or F
- `classrooms`: ManyToMany to Classroom (`related_name='teachers'`)

### 👨‍🎓 Student
- `first_name`, `last_name`
- `gender`: M or F
- `classroom`: ForeignKey to Classroom (`related_name='students'`)

---

## 📌 Features

- Create / List / Retrieve / Update / Delete:
  - Schools
  - Classrooms
  - Teachers
  - Students

- **Filtering via query parameters:**
  - School: `?name=...`
  - Classroom: `?school=...`
  - Teacher: `?school=...&classroom=...&first_name=...&gender=...`
  - Student: `?school=...&classroom=...&first_name=...&gender=...`

- **Detailed Views:**
  - School detail includes: number of classrooms, teachers, and students
  - Classroom detail includes: list of teachers and students
  - Teacher detail includes: list of classrooms they teach
  - Student detail includes: classroom info

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/arrkpong/Test-Swift-Dynamics.git
```

### 2. Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start the Development Server
```bash
python manage.py runserver
```

### 5. Open in Browser
```bash
http://127.0.0.1:8000/
```

## 🔍 API Endpoints
```bash
Resource	    Endpoint	    Description
School	        /schools/	    List / Create
                /schools/<id>/	Retrieve / Update / Delete
Classroom	    /classrooms/	List / Create
Teacher	        /teachers/	    List / Create
Student	        /students/	    List / Create
```