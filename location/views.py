from rest_framework import viewsets
from .models import Library, Rack
from .serializers import LibrarySerializer, RackSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]