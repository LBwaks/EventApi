from rest_framework import serializers
from django.contrib.auth.models import User 
from events.serializers import EventSerializer
from .models import Profile
from phonenumber_field.serializerfields import PhoneNumberField


# from rest_framework.serializers import ValidationError
# from phonenumber_field.serializerfields import PhoneNumberField
# from phonenumber_field.phonenumber import to_python


# class CustomPhoneNumberField(PhoneNumberField):
#     def to_internal_value(self, data):
#         phone_number = to_python(data)
#         if phone_number and not phone_number.is_valid():
#             raise ValidationError(self.error_messages["invalid"])
#         return phone_number.as_e164

class PhoneNumberSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(region="KE")
    
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields =('id','user','type_of_user','name','phone_number',
        'gender','type_of_artist','type_of_organization','type_of_venue','city','town','bio',
        'profile',
        'facebook', 'twitter','instagram','website')
        read_only_fields =['user']
        
   

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
