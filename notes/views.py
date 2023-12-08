from django.shortcuts import render
from .models import Note, Category

def home(request):
    notes = Note.objects.all()
    categories = Category.objects.all()
    return render(request, 'notes/home.html', {'notes': notes, 'categories': categories})
