from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'cover_image']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ratings', 'content']