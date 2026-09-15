import os
import django

# Tell Django where the settings.py file is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

# Initialize Django
django.setup()

# NOW we can import our models
from books_outlet.models import Address, Author, Book


def seed_database():

    # ==========================================================
    # ADDRESSES
    # ==========================================================

    addresses_data = [
        {
            "street": "221B Baker Street",
            "postal_code": "NW1 6XE",
            "city": "London",
        },
        {
            "street": "13 Victoria Street",
            "postal_code": "W1H 1AW",
            "city": "London",
        },
        {
            "street": "Bag End",
            "postal_code": "HOB 001",
            "city": "Hobbiton",
        },
        {
            "street": "42 Elm Street",
            "postal_code": "10001",
            "city": "New York",
        },
        {
            "street": "15 Oak Avenue",
            "postal_code": "60601",
            "city": "Chicago",
        },
        {
            "street": "27 High Street",
            "postal_code": "OX1 1AA",
            "city": "Oxford",
        },
        {
            "street": "39 Peabody Street",
            "postal_code": "MA 02130",
            "city": "Boston",
        },
        {
            "street": "10 Yasnaya Street",
            "postal_code": "301000",
            "city": "Tula",
        },
    ]

    addresses = []

    for address_data in addresses_data:

        address, created = Address.objects.get_or_create(
            street=address_data["street"],
            postal_code=address_data["postal_code"],
            city=address_data["city"],
        )

        addresses.append(address)

        if created:
            print(f"Created address: " f"{address.street}, {address.city}")

    # ==========================================================
    # AUTHORS
    # ==========================================================

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

    authors = {}

    for index, (first_name, last_name) in enumerate(authors_data):

        author, created = Author.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            defaults={
                "address": addresses[index],
            },
        )
        if not author.address and index < len(addresses):
            author.address = addresses[index]
            author.save()

        authors[f"{first_name} {last_name}"] = author

        if created:
            print(f"Created author: " f"{author.first_name} {author.last_name}")

    # ==========================================================
    # BOOKS
    # ==========================================================

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

        book, created = Book.objects.get_or_create(
            title=title,
            defaults={
                "rating": rating,
                "author": authors[author_name],
                "is_bestSelling": is_best_selling,
            },
        )

        if created:
            print(f"Created book: {book.title}")

    print("\nDatabase seeded successfully!")


if __name__ == "__main__":
    seed_database()
