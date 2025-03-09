from rest_framework import serializers
from .models import User, Post


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'like']
        read_only_fields = ['author', 'like']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validate_data):
        user= User.objects.create_user(username=validate_data['username'], email=validate_data['email'], password=validate_data['password'])
        return user


