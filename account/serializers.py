from rest_framework import serializers
from .models import User


class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =  ("id", "email", "password", "first_name", "last_name", "phone_number", "address",
                    "date_joined", "last_login"
                  )

        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
        } 

    def create(self, validated_data):
        user = User(**validated_data)
        user.is_member = True
        user.set_password(validated_data["password"])
        user.save()
        return user

    


class LibrarianSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =  ("id", "email", "password", "first_name", "last_name", "phone_number", "address",
                    "date_joined", "last_login"
                  )

        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
        } 

    def create(self, validated_data):
        user = User(**validated_data)
        user.is_staff = True
        user.is_librarian = True
        user.set_password(validated_data["password"])
        user.save()
        return user

