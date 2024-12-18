from django.urls import path

from .views import index, about, contact, book_details, new_boook, delete_book, edit_book

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('book_details/<int:book_id>/', book_details, name="book_details" ),
    path('new_book/', new_boook, name="new_book"),
    path('delete_book/<int:book_id>/', delete_book, name="delete_book"),
    path('edit_book/<int:book_id>/', edit_book, name="edit_book")
    
]
