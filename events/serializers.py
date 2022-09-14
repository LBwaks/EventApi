from cgitb import lookup
from rest_framework import serializers
from .models import Event,Tag,Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelField):
    # category = CategorySerializer(read_only = True, many =True)
    # tag =EventSerializer(read_only = True, many =True)
    # event =EventSerializer(read_only = True, many =True)
    class Meta:
        model = User
        fields = ['id','username']

class TagSerializer(serializers.ModelSerializer):
    # events =EventSerializer(read_only = True, many =True)
    class Meta:
        model = ['name','slug','events']
        lookup_field = 'slug'
        extra_kwargs = {
            'url':{'view_name':'tag-detail','lookup_field':'slug'}
        }

class EventSerializer(serializers.ModelSerializer):
    # tag = TagSerializer(many=True)
    # owner = UserSerializer( many=True, read_only=True)

    class Meta:
        model = Event 
        fields = ['id','event_id','url',
        # 'owner',
        'user','tag','name','slug','description','type',
                 'start_date','end_date','county','town','address','venue','charge',
                 'max_attendees','event_host' ,'event_partners','main_speaker_artist',
                 'other_speaker_artist','bookmark','likes','is_featured','is_published','updated_date','created_date']
        read_only_fields =['user','event_id']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'view_name':'event-detail','lookup_field': 'slug'}
        }
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['event_likes'] = instance.likes.count()
            return representation


    def validate(self,data):
        if data['start_date'] == data['end_date']:
            raise serializers.ValidationError('Event Start Data Cannot Be Same As Event End Date')
        elif data['start_date'] > data['end_date']:
            raise serializers.ValidationError('Event End Date less Than start date ')
        
        return data


    def validate_name(self,value):
        if len(value) < 4:
            raise serializers.ValidationError('Event Name Must Contain More Than 4 characters')
        return value
    def validate_description(self,value):
        if len(value) < 100:
            raise serializers.ValidationError('Event Description Must Contain more than 100 characters')
        return value

    def validate_town(self,value):
        if len(value)< 3:
            raise serializers.ValidationError('Town Must Contain more than three characters')
        return value
    def validate_address(self,value):
        if len(value)< 3:
            raise serializers.ValidationError('Address Must Contain more than three characters')
        return value
    def validate_venue(self,value):
        if len(value)< 3:
            raise serializers.ValidationError('Venue Must Contain more than three characters')
        return value
    def validate_event_host(self,value):
        if value and len(value)< 3:
            raise serializers.ValidationError('Event Host Must Contain more than three characters')
        return value
    def validate_event_partners(self,value):
        if value and len(value)< 3:
            raise serializers.ValidationError('Event Partners Must Contain more than three characters')
        return value
    def validate_main_speaker_artist(self,value):
        if value and len(value)< 3:
            raise serializers.ValidationError('Main Speaker/Artist Must Contain more than three characters')
        return value
    def validate_other_speaker_artist(self,value):
        if value and len(value)< 3:
            raise serializers.ValidationError('Other Speaker/Artist Must Contain more than three characters')
        return value
   
class TagSerializer(serializers.ModelSerializer):
    # events =EventSerializer(read_only = True, many =True)
    class Meta:
        model = ['name','url','slug','events']
        # lookup_field = 'slug'
        extra_kwargs = {
            'url':{'view_name':'tag-detail','lookup_field':'slug'}
        }


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
