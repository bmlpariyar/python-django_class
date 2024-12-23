from django.urls import path

from .views import index, about, contact, book_details, new_boook, delete_book, edit_book, add_review, delete_review, edit_review

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('book_details/<int:book_id>/', book_details, name="book_details" ),
    path('new_book/', new_boook, name="new_book"),
    path('delete_book/<int:book_id>/', delete_book, name="delete_book"),
    path('edit_book/<int:book_id>/', edit_book, name="edit_book"),
    path('add_review/<int:book_id>', add_review, name="add_review"),
    path('delete_review/<int:review_id>/', delete_review, name="delete_review"),
    path('edit_review/<int:review_id>/',edit_review, name="edit_review" ),
    
]
