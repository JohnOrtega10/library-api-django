from rest_framework import serializers
from .models import Editorial, Author

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
