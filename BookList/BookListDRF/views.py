from django.shortcuts import render
from .serializer import BookSerializer
from rest_framework import generics
from .models import Book

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_calss = BookSerializer