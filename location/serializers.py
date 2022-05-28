from rest_framework import serializers
from .models import Library, Rack

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'