import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
django.setup()

from books_outlet.models import Author, Book


def seed_database():

    authors_data = [
        ("J.K.", "Rowling"),
        ("George", "Orwell"),
        ("J.R.R.", "Tolkien"),
        ("Harper", "Lee"),
        ("F. Scott", "Fitzgerald"),
        ("Jane", "Austen"),
        ("Ernest", "Hemingway"),
        ("Leo", "Tolstoy"),
    ]

    # -----------------------------------------------
    # Create Authors
    # -----------------------------------------------

    authors = {}

    for first_name, last_name in authors_data:

        author, created = Author.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
        )

        authors[f"{first_name} {last_name}"] = author

        if created:
            print(f"Created author: {first_name} {last_name}")
        else:
            print(f"Author already exists: {first_name} {last_name}")

    # -----------------------------------------------
    # Create Books
    # -----------------------------------------------

    books_data = [
        (
            "Harry Potter and the Philosopher's Stone",
            5,
            "J.K. Rowling",
            True,
        ),
        (
            "Harry Potter and the Chamber of Secrets",
            5,
            "J.K. Rowling",
            True,
        ),
        (
            "Harry Potter and the Prisoner of Azkaban",
            5,
            "J.K. Rowling",
            True,
        ),
        (
            "1984",
            5,
            "George Orwell",
            True,
        ),
        (
            "Animal Farm",
            4,
            "George Orwell",
            True,
        ),
        (
            "The Hobbit",
            5,
            "J.R.R. Tolkien",
            True,
        ),
        (
            "The Lord of the Rings",
            5,
            "J.R.R. Tolkien",
            True,
        ),
        (
            "To Kill a Mockingbird",
            5,
            "Harper Lee",
            True,
        ),
        (
            "The Great Gatsby",
            4,
            "F. Scott Fitzgerald",
            False,
        ),
        (
            "Pride and Prejudice",
            5,
            "Jane Austen",
            True,
        ),
        (
            "The Old Man and the Sea",
            4,
            "Ernest Hemingway",
            False,
        ),
        (
            "War and Peace",
            5,
            "Leo Tolstoy",
            True,
        ),
    ]

    for title, rating, author_name, is_best_selling in books_data:

        author = authors[author_name]

        book, created = Book.objects.get_or_create(
            title=title,
            defaults={
                "rating": rating,
                "author": author,
                "is_bestSelling": is_best_selling,
            },
        )

        if created:
            print(f"Created book: {title}")
        else:
            print(f"Book already exists: {title}")

    print("\nDatabase seeding completed!")


if __name__ == "__main__":
    seed_database()
