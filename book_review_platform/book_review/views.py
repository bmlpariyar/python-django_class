from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')



def book_details(request, book_id):
    books = Book.objects.get(id=book_id)
    context = {'book': books}
    return render(request, 'book_details.html', context)
