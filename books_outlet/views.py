from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg


# Create your views here.
def index(req):
    books = Book.objects.all().order_by(
        "-rating"
    )  # By Default Ascending// For Decending - Add a Minus as ("-param")

    # We will not write query again since it degrades performance
    num_of_books = books.count()
    average_rating = books.aggregate(Avg("rating"))  # aggregate(Func("parameter"))
    return render(
        req,
        "book_outlet/index.html",
        {"books": books, "average_rating": average_rating, "no_of_books": num_of_books},
    )


def book_detail(req, slug):
    """
    Returns Book Detail Page
    """
    book = get_object_or_404(Book, slug=slug)
    return render(req, "book_outlet/book_detail.html", {"book": book})
