from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['id','username']

class BookingSerializer(serializers.ModelSerializer):
    # url =serializers.HyperlinkedIdentityField(view_name='booking-detail',lookup_field = 'uuid')
    class Meta :
        model= Booking
        fields =['uuid',
                 'user',
                #  'url',
                 'event_id','tickets','status','updated_at','created_at']
        read_only_fields =['uuid',
                           'user',
                           'event_id','status',]
        lookup_field = 'uuid'
        extra_kwargs = {
            'url' : {'view_name':'booking-detail','lookup_field': 'uuid'}
        }