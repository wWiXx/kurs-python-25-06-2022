from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from books.services import book_service
from books.utils import read_from_csv

allbooks = [
    {"tytul": "pan tadeusz", "autor": "adam mickiewicz", "rok_wydania": 2022, "liczna_stron": 477},
    {"tytul": "lalka", "autor": "bolesław prus", "rok_wydania": 1891, "liczna_stron": 679},
    {"tytul": "maly ksiaze", "autor": "antoine de sain exupery", "rok_wydania": 2022, "liczna_stron": 477},
]


def listview(request):
    print(request.GET)
    q = request.GET.get("q")
    print(q)
    if q:
        books = book_service.filter(q=q)
    else:
        books = book_service.get_all_books()
    return render(
        request,
        "books/bookspage.html",
        {"books": books},
    )


def details(request, book_id):
    book = book_service.get_book(book_id)
    return render(
        request,
        "books/details.html",
        {"book": book},
    )
