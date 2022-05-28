from rest_framework import serializers
from .models import Book, BookItem
# from location.serializers import LibrarySerializer
from material_data.serializers import EditorialSerializer

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')
    language = serializers.CharField(source='get_language_display')

    class Meta:
        model = Book
        fields = "__all__"


class ListBookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')
    language = serializers.CharField(source='get_language_display')

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
    
class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields =  "__all__"
      

class ListBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields =  "__all__"
        depth = 2
    

