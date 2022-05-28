
from rest_framework import viewsets
from book.models import BookItem
from .models import BookLending, BookReservation
from .serializers import ListBookLendingSerializer, BookLendingSerializer, BookReservationSerializer, ListBookReservationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from  rest_framework import status

class BookLendingViewSet(viewsets.ModelViewSet):
    queryset = BookLending.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]
    def get_serializer_class(self):
        if self.action != "list" and self.action != "retrieve":
            return BookLendingSerializer
        else:
            return ListBookLendingSerializer

    def create(self, request, *args, **kwargs):
            book_item = BookItem.objects.get(pk=request.data["book_item"]) 
            if  book_item.is_rent or book_item.is_reserve:
                return Response({"message":"This book is already rented or reserved"}, status=status.HTTP_400_BAD_REQUEST)

            num_rents = BookLending.objects.filter(member__id = request.data["member"], is_return = False).count()
            if num_rents >= 5:
                return Response({"message":"Exceeds the limit of books that can be rented"}, status=status.HTTP_400_BAD_REQUEST)
           
            data = request.data
            serializer = BookLendingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
   


class BookReservationViewSet(viewsets.ModelViewSet):
    queryset = BookReservation.objects.all()
    serializer_class = BookReservationSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.action != "list" and self.action != "retrieve":
            return BookReservationSerializer
        else:
            return ListBookReservationSerializer

    def create(self, request, *args, **kwargs):
            book_item = BookItem.objects.get(pk=request.data["book_item"]) 
            if  book_item.is_rent or book_item.is_reserve:
                return Response({"message":"This book is already rented or reserved"}, status=status.HTTP_400_BAD_REQUEST)

            num_reserves = BookReservation.objects.filter(member__id = request.data["member"], status = False).count()
            if num_reserves >= 2:
                return Response({"message":"Exceeds the limit of books that can be reserved"}, status=status.HTTP_400_BAD_REQUEST)
           
            data = request.data
            serializer = BookReservationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

