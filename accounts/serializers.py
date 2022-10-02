from rest_framework import serializers
from django.contrib.auth.models import User 
from events.serializers import EventSerializer
from .models import Profile
    
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields =('id','user','fname','lname')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # event = serializers.HyperlinkedRelatedField(view_name='event-detail',read_only =True, many=True )

    class Meta:
        model = User 
        fields =('id','url','username', #'event'
        )
        # extra_kwargs ={
        #     'events':{'view_name':'event-detail',#'lookup_field':'username'
        #     }
        #     }
