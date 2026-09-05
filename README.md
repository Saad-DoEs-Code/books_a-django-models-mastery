# Books Outlet - Django Models & Data Mastery

A Django web application built to master Django Models, Object-Relational Mapping (ORM), database queries, data aggregations, dynamic URL routing, and custom model methods. Developed following the "Data and Models" module of Maximilian Schwarzmuller's Django Course.

---

## Technical Notes & Key Learnings

### 1. Django Models & Schema Definition
Django models map Python classes directly to database tables. Attributes within the class represent table columns.

- **Model Declaration**: Inheriting from `models.Model` converts a standard Python class into a Django database model.
- **Data Types**:
  - `CharField`: For short text strings with a required `max_length`.
  - `IntegerField`: For whole numbers, combined with validators for range enforcement.
  - `BooleanField`: For storing boolean true/false flags (e.g., `is_bestSelling`).
  - `SlugField`: For URL-friendly identifiers indexed with `db_index=True` for faster database query lookups.

### 2. Validation & Field Constraints
Field validators enforce business logic constraints directly at the model level before data persistence:
- `MinValueValidator(1)` and `MaxValueValidator(5)` ensure ratings stay within a 1 to 5 range.
- `db_index=True` creates database indexes on frequently queried fields like `slug`.

### 3. Model Methods & Dynamic Routing
- **Slug Generation**: Overriding the model's `save()` method allows automatically generating slug strings from title attributes using `django.utils.text.slugify`.
- **Absolute URLs**: Implementing `get_absolute_url()` uses `django.urls.reverse` to decouple URL paths from template links, creating maintainable, canonical URLs for individual book detail views.

### 4. Django ORM & Database Aggregations
Django's QuerySet API enables database interactions without writing raw SQL queries.

- **Querying & Ordering**:
  ```python
  books = Book.objects.all().order_by("-rating")
  ```
  `order_by("-rating")` sorts books in descending order by rating.

- **Efficient Record Counting**:
  ```python
  num_of_books = books.count()
  ```
  Using `.count()` performs an optimized SQL `COUNT()` operation rather than loading all model instances into Python memory.

- **Database Aggregations**:
  ```python
  from django.db.models import Avg

  average_rating = books.aggregate(Avg("rating"))
  ```
  The `.aggregate()` method computes summary values across QuerySets, returning a dictionary such as `{'rating__avg': 4.5}`.

### 5. View Logic & Error Handling
- **`get_object_or_404`**: Ensures reliable HTTP 404 responses when a requested book slug is not present in the database.
- **Context Passing**: Aggregated metrics and queryset arrays are passed to HTML templates seamlessly via context dictionaries.

---

## Project Structure

```
books/
├── manage.py
├── books/                  # Project Configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── books_outlet/           # Main Application App
    ├── models.py           # Book Data Model & Custom Methods
    ├── views.py            # Catalog Index & Book Detail Views
    ├── urls.py             # App Route Definitions
    ├── static/
    │   └── books_outlet/
    │       └── styles.css  # Modern Glassmorphic Styling System
    └── templates/
        └── book_outlet/
            ├── base.html       # Base Template with Navigation
            ├── index.html      # Catalog Overview & Stat Badges
            └── book_detail.html# Individual Book Details Page
```

---

## Setup & Local Execution

### Prerequisites
- Python 3.10+
- Django 4.x or Django 5.x

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Saad-DoEs-Code/books_a-django-models-mastery.git
   cd books_a-django-models-mastery
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

## Course Reference
This project was built following the **Data and Models** module of *Python Django - The Practical Guide* by Maximilian Schwarzmuller.
