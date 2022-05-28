from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, BookItem
from .serializers import BookItemSerializer, BookSerializer, ListBookItemSerializer, ListBookSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsLibrarianOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.action != "list" and self.action != "retrieve":
            return BookSerializer
        else:
            return ListBookSerializer

class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsLibrarianOrReadOnly]

    def get_serializer_class(self):
        if self.action != "list" and self.action != "retrieve":
            return BookItemSerializer
        else:
            return ListBookItemSerializer

    filterset_fields = ['library', 'book__title', 'book__authors','book__category', 
                        'book__language', 'book__editorial', 'book__year_publication']
   





    