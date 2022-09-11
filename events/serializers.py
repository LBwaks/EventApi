from rest_framework import serializers
from .models import Event,Tag,Category
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ['id','user','tag','event_id','name','slug','description','type',
                 'start_date','end_date','county','town','address','venue','charge',
                 'max_attendees','event_host' ,'event_partners','main_speaker_artist',
                 'other_speaker_artist','bookmark','likes','is_featured','is_published','updated_date','created_date']
        read_only_fields =['user','slug',]
        # def validate(self,attrs):
        #     attrs['user']= self.context['request'].user
        #     return attrs

class TagSerializer(serializers.ModelSerializer):
    events =EventSerializer(read_only = True, many =True)
    class Meta:
        model = ['name','slug','events']


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
