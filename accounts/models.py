from fileinput import filename
from django.conf import Settings
from django.db import models
from  django.conf import settings
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
User = settings.AUTH_USER_MODEL
from django_extensions.db.fields import AutoSlugField
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.


def my_slugify_function(content):
    return content.replace('_', '-').lower()

def upload_to(instance,filename):
    return 'profiles/{filename}'.format(filename=filename)

class Profile(models.Model):  
    class UserType(models.TextChoices):
        ARTIST = 'ARTISTS' ,'ARTIST'
        VENUE = 'VENUE' ,'VENUE'
        ORGANIZATION = 'ORGANIZATION','ORGANIZATION'
        EVENT = 'EVENT' ,'EVENT' 
    class GenderType(models.TextChoices):
        MALE = 'MALE','MALE'
        FEMALE ='FEMALE','FEMALE'
        OTHER = 'OTHER','Prefer Not To Say' 
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    type_of_user = models.CharField(_("User Category"),choices = UserType.choices, max_length=50)
    name = models.CharField(_("Full Name"), max_length=50)
    slug = AutoSlugField(populate_from='name', slugify_function=my_slugify_function)
    phone_number = PhoneNumberField(blank=True)
    gender = models.CharField(_("Gender"), max_length=50,choices = GenderType.choices,blank=True)    
    type_of_artist = models.CharField(_("Artist Category"), max_length=50,blank=True)
    type_of_organization =models.CharField(_("Organisation Category"), max_length=50,blank=True)
    type_of_venue =models.CharField(_("Venue Category"), max_length=50,blank=True)
    city =models.CharField(_("Town/City"), max_length=50,blank=True)
    town =models.CharField(_("Location"), max_length=50,blank=True)
    bio = models.TextField(_("Bio"),blank=True)
    profile = models.ImageField(_("Profile"), upload_to=upload_to, height_field=None, width_field=None, max_length=None,blank=True)
    facebook = models.URLField(_("Facebook"), max_length=200,blank=True)
    twitter = models.URLField(_("Twitter"), max_length=200,blank=True)
    instagram =models.URLField(_("Instagram"), max_length=200,blank=True)
    website =models.URLField(_("Your Website"), max_length=200,blank=True)
    updated_date =models.DateTimeField( auto_now=True )    
    created_date =models.DateTimeField(auto_now_add =True)   

    def __str__(self):
        return self.user.username

@receiver(post_save ,sender = User)
def create_user_profile(sender, instance ,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save ,sender = User)
# def save_user_profile(sender,instance ,**kwargs):
#     instance.profile.save()

    