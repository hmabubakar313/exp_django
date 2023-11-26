from .models import *
from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate_name(self,value):
        if (len(value)<3):
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return
    

    def validate_email(self,value):
        try:
            validate_email(value)
        except DjangoValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        return value


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'

    
    def validate_title(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Title cannot be empty")
        return value

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        