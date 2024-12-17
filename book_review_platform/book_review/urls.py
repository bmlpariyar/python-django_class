from django.urls import path

from .views import index, about, contact, book_details

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('book_details/<int:book_id>/', book_details, name="book_details" )
]
