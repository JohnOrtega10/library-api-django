from rest_framework import viewsets
from .models import Editorial, Author
from .serializers import EditorialSerializer, AuthorSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]     

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]