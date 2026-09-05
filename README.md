# Django Models & Data Mastery - Book Outlet Project

## Project Overview
A comprehensive Django web application developed during the "Data and Models" module of Maximilian Schwarzmuller's Django course. This project demonstrates how Django handles database abstractions, ORM queries, data model field types, field validations, slug generation, relationships, and aggregations, paired with a modern UI presentation.

---

## Key Learning Outcomes & Technical Reference Notes

### 1. Django Models & Schema Design
- **`models.Model` Base Class**: Defining database tables as Python classes.
- **Field Types & Attributes**:
  - `CharField(max_length=...)`: Short to medium length text fields.
  - `IntegerField(validators=[...])`: Numeric values with min/max validation boundaries (`MinValueValidator`, `MaxValueValidator`).
  - `BooleanField(default=...)`: Storing boolean flags such as bestseller status.
  - `SlugField(default="", blank=True, null=False, db_index=True)`: URL-friendly identifier field indexed for fast database lookups.
- **String Representation (`__str__`)**: Overriding the `__str__` method for readable object representation in Django shell and admin panel.

### 2. Auto-Generating Slugs (`save()` Method Override)
- Using `django.utils.text.slugify` inside model overrides:
  ```python
  def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
  ```
- Ensuring URLs are clean, human-readable, and SEO-friendly (`/book-details-page-slug` instead of `/1`).

### 3. Absolute URL Routing (`get_absolute_url`)
- Standard Django pattern for object canonical URLs:
  ```python
  def get_absolute_url(self):
      return reverse("book-detail", args=[self.slug])
  ```
- Used directly in Django templates (`{{ book.get_absolute_url }}`) to keep URL routing DRY (Don't Repeat Yourself).

### 4. Database Aggregations & QuerySets
- **Ordering QuerySets**: `Book.objects.all().order_by("-rating")` for descending order sorting.
- **Aggregating Metrics**: Utilizing `django.db.models.Avg`, `Count`, `Min`, `Max` to perform database-level operations:
  ```python
  num_of_books = books.count()
  average_rating = books.aggregate(Avg("rating"))
  ```
- **Performance Considerations**: Computing counts and averages directly in SQL via Django ORM avoids loading entire QuerySets into Python memory.

### 5. Views & Template Layer
- **`get_object_or_404`**: Clean error handling returning HTTP 404 response when a lookup slug does not exist.
- **Template Filters**:
  - `pluralize`: Adding dynamic 's' based on list length.
  - `floatformat:1`: Formatting floating-point values for user interface display.
  - `default`: Fallback value handling for empty context variables.

---

## Project Structure
```
books/
│
├── books/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── books_outlet/
│   ├── migrations/
│   ├── static/
│   │   └── books_outlet/
│   │       └── styles.css
│   ├── templates/
│   │   └── book_outlet/
│   │       ├── base.html
│   │       ├── book_detail.html
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── .gitignore
└── README.md
```

---

## Setup & Local Development Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps
1. **Clone Repository**:
   ```bash
   git clone https://github.com/Saad-DoEs-Code/books_a-django-models-mastery.git
   cd books_a-django-models-mastery
   ```

2. **Create Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```
   Open your browser at `http://127.0.0.1:8000/`.

---

## Credits
- Course: **Django - The Practical Guide** by Maximilian Schwarzmuller.
- Module: **Data & Models**.
