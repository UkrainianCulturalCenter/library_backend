from django.http import HttpRequest, HttpResponse
from django.shortcuts import render  # noqa
from .models import Book, Author


def index(request: HttpRequest) -> HttpResponse:
    num_all_books = Book.objects.count()
    num_all_authors = Author.objects.count()
    context = {
        "num_all_authors": num_all_authors,
        "num_all_books": num_all_books,
    }
    return render(request, "catalog/index.html", context=context)
