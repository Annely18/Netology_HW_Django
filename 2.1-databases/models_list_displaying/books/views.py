from django.shortcuts import render
from books.models import Book

def books_view1(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books_view(request):
    template = 'books/books.html'
    book_obj = Book.objects.all()
    context = {'books': book_obj}
    return render(request, template, context)


def pub_date_view(request, req_pub_date):
    template = 'books/pub_date.html'
    book_obj = Book.objects.filter(pub_date=req_pub_date)
    prev_date = Book.objects.filter(pub_date__lt=req_pub_date).first()
    next_date = Book.objects.filter(pub_date__gt=req_pub_date).first()
    context = {'books': book_obj, 'prev_date': prev_date, 'next_date': next_date}
    return render(request, template, context)

