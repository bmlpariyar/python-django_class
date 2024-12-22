from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from .forms import BookForm
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
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.all()
    context = {'book': book, 'reviews': reviews}
    return render(request, 'book_details.html', context)


def new_boook(request):
    if request.method == "POST":
        form= BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'new_book.html', context)



def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("home")


def edit_book(request, book_id):
    book=Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'new_book.html', context)
    
