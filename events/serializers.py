from rest_framework import serializers
from .models import Event,Tag,Category
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    event =EventSerializer(read_only = True, many =True)
    class Meta:
        model = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    tag =TagSerializer(read_only = True, many =True)
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelField):
    category = CategorySerializer(read_only = True, many =True)
    tag =EventSerializer(read_only = True, many =True)
    event =EventSerializer(read_only = True, many =True)
    class Meta:
        model = User
        fields = '__all__'
