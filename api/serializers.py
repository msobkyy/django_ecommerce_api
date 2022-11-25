from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Categorys
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# serializers overview


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = '__all__'


