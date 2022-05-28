from dataclasses import field
from rest_framework import serializers

from book.serializers import BookItemSerializer, ListBookItemSerializer
from .models import BookLending, BookReservation
from account.serializers import MemberSerializer

class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = '__all__'
     


class ListBookLendingSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    book_item = ListBookItemSerializer()
    class Meta:
        model = BookLending
        fields = '__all__'

class BookReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReservation
        fields = '__all__'

class ListBookReservationSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    book_item = ListBookItemSerializer()
    class Meta:
        model = BookReservation
        fields = '__all__'