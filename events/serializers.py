from cgitb import lookup
from rest_framework import serializers
from django.contrib.auth.models import User
from bookings.models import Booking
from .models import Event,Tag,Category,Comment,EventImage
# from bookings.serializers import BookingSerializer




class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields =['id','event','user','content','created_at']
        read_only_fields =['user']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tag-detail',
        # lookup_field='slug'
    )
    comments =CommentSerializer(many =True,read_only=True)
    remaining_slots = serializers.SerializerMethodField()
    # booked_slots = BookingSerializer(source = 'bookings',many=True)
    booked_slots = serializers.SerializerMethodField()

    class Meta:
        model = Event 
        fields = ['slots','booked_slots','remaining_slots',
                #   'booked_slots',
                  'id','event_id','url',
        
        'user',
        'tags',
        'name','slug','description','type',
                 'start_date','end_date','county','town','address','venue','charge','slots',
                 'max_attendees','event_host' ,'event_partners','main_speaker_artist',
                 'other_speaker_artist','bookmark','comments','likes','is_featured','is_published','updated_date','created_date']
        read_only_fields =['user','event_id']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'view_name':'event-detail','lookup_field': 'slug'},
            'tags':{'view_name':'tag-detail','lookup_field': 'slug'}
        }
    def to_representation(self, instance):
            representation = super(EventSerializer,self).to_representation(instance)
            # representation['likes'] = instance.likes.count()
            representation['event_comments']=instance.comments.count()
            # representation['start_date'] = instance.start_date.strftime("%d-%m-%Y")
            # representation['end_date'] = instance.end_date.strftime("%d-%m-%Y")
            # representation['bookmarks'] = instance.bookmark.count()
            return representation
        
    def get_remaining_slots(self,obj):
        slots = Booking.objects.filter(event_id = obj.id).count()
        if slots  != obj.slots:
            remaining_slots = 0
            remaining_slots = (obj.slots - slots)
            return remaining_slots
    
    def get_booked_slots(self,obj):
        slots = Booking.objects.filter(event_id = obj.id)
        return slots.count()

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
    events =EventSerializer(read_only = True, many =True)
    class Meta:
        model = Tag
        fields = ['name','url','slug','events']
        lookup_field = 'slug'
        extra_kwargs = {
            # 'url':{'view_name':'event:tag-detail', 'lookup_field':'slug'}
        }
# class CategorySerializer(serializers.ModelSerializer):
#     # tag =TagSerializer(read_only = True, many =True)
#     class Meta:
#         model = Category
#         fields = '__all__'


