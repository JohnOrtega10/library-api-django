from rest_framework import viewsets
from rest_framework.decorators import action
from member_request.models import BookLending, BookReservation
from member_request.serializers import BookLendingSerializer, BookReservationSerializer
from .serializers import LibrarianSerializer, MemberSerializer
from .models import User
from rest_framework.response import Response
from  rest_framework import status
from .permissions import IsOwner
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class MemberAccountViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset =  User.objects.filter(is_member=True)

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner, IsAuthenticated]
        return [permission() for permission in permission_classes]
        
    # @action(detail=True)
    # def my_rents(self, request, pk=None):
    #     rents = BookLending.objects.filter(member__id = pk, is_return=False).values_list("book_item__id", flat=True)
    #     books_item = BookItem.objects.filter(id__in = rents).values_list("book__id", flat=True)
    #     books = Book.objects.filter(id__in = books_item)
    #     serializer = BookSerializer(books, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True)
    def my_rents(self, request, pk=None):
        rents = BookLending.objects.filter(member__id = pk, is_return=False)
        serializer = BookLendingSerializer(rents, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def my_reservations(self, request, pk=None):
        reserves = BookReservation.objects.filter(member__id = pk, status = False)
        serializer = BookReservationSerializer(reserves, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LibrarianAccountViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarianSerializer
    queryset =  User.objects.filter(is_librarian=True)

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser, IsAuthenticated]
        else:
            permission_classes = [IsOwner, IsAuthenticated]
        return [permission() for permission in permission_classes]
