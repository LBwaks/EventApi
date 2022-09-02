from pyexpat import model
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from .choices import county,types
from django.db.models.signals import pre_save
# from 
import random ,string

# Create your models here.
User = settings.AUTH_USER_MODEL

class CategoryManager(models.Manager):
    def published(self):
        return self.filter(is_published = True)

class Category(models.Model):
    user =models.ForeignKey(User,editable=False,related_name='events_category', on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length= 50, unique=True)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField(max_length= 250)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    user =models.ForeignKey(User,editable=False,on_delete =models.CASCADE,null=False)
    category =models .ForeignKey(Category,related_name='category_tag',on_delete=models.CASCADE,null = False)
    name = models.CharField(max_length= 50,unique=True)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField(max_length= 250)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    # category = CategoryManager()
    # objects =models.Manager()
    

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify('name')
        return super().save(*args, **kwargs)

class TagManager(models.Manager):
    def published(self):
        return self.filter(is_published = True)


def random_string_generotor(size=10,chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_event_id_generation(instance):
    new_event_id = random_string_generotor().upper()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(event_id = new_event_id).exists()
    if qs_exists:
        return unique_event_id_generation(instance)
    return new_event_id

class Event(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    tag = models.ForeignKey(Tag, related_name='event_tag',on_delete=models.CASCADE,null=False)
    event_id = models.CharField(blank=True, max_length= 30)
    # hitcount =
    name = models.CharField(max_length=50,blank= False,null=False)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField()
    type = models.CharField(choices=types,max_length=20)

#  date and time
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField(blank= True,null=True)
    end_time = models.TimeField(blank= True,null=True)

# location 
    county = models.CharField(choices=county, max_length=20,default='Nairobi')
    town = models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    # get_maps =

    charge = models.IntegerField()
    max_attendees = models.IntegerField(blank= True,null=True)

    event_host = models.CharField(max_length=50,blank= True,null=True)
    event_partners = models.CharField(max_length=50,blank= True,null=True)

    main_speaker_artist =models.CharField(max_length=50,blank= True,null=True)
    other_speaker_artist = models.CharField(max_length=50,blank=True,null=True)

    likes= models.IntegerField(blank= True,null=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    updated_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # objects =models.Manager()
    # tag = TagManager()

    def __str__(self):
        return self.name


def pre_save_event_id(sender,instance,*args, **kwargs):
    if not instance.event_id:
        instance.event_id =unique_event_id_generation(instance)
pre_save.connect(pre_save_event_id,sender=Event)

