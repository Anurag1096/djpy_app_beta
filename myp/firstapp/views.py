from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializers
from django.shortcuts import render

def home(request):
    return render(request, "firstapp/home.html") 


def about(request):
    return render(request, 'firstapp/about.html')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

