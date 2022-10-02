from django.conf import Settings
from django.db import models
from  django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
from django_extensions.db.fields import AutoSlugField


def my_slugify_function(content):
    return content.replace('_', '-').lower()

class Profile(models.Model):    
    user = models.OneToOneField(User,on_delete=models.CASCADE)   
    # slug 
    fname = models.CharField(max_length=250 )
    slug = AutoSlugField(populate_from=['fname','lname'], slugify_function=my_slugify_function)
    lname = models.CharField(max_length=250) 
    created_date =models.DateTimeField(auto_now_add =True)   

    def __str__(self):
       return self.fname
    