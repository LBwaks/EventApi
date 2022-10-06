from pyexpat import model
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from .choices import county,types
from django.db.models.signals import pre_save
from .managers import PublishedEventsManager,PublishedTagManager,PublishedCategoryManager
import random ,string
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

# Create your models here.
User = settings.AUTH_USER_MODEL

def my_slugify_function(content):
    return content.replace('_', '-').lower()

class Category(models.Model):
    user =models.ForeignKey(User,editable=False,related_name='events_category', on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length= 50, unique=True)
    slug = AutoSlugField(populate_from='name', slugify_function=my_slugify_function)
    description = models.TextField(max_length= 250)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    objects =models.Manager()
    publishedCategory = PublishedCategoryManager()
    
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
    slug = AutoSlugField(populate_from='name', slugify_function=my_slugify_function)
    description = models.TextField(max_length= 250)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    
    objects =models.Manager()
    publishedTags = PublishedTagManager()
    

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify('name')
        return super().save(*args, **kwargs)




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
    tag = models.ManyToManyField(Tag, related_name='event_tag')
    event_id = models.CharField(blank=True, max_length= 30)
    # hitcount =
    name = models.CharField( max_length=50)
    slug = AutoSlugField(populate_from=['name','event_id'], slugify_function=my_slugify_function)
    description = models.TextField()
    type = models.CharField(choices=types,max_length=20)

#  date and time
    start_date = models.DateTimeField()
    # start_time = models.TimeField()
    end_date = models.DateTimeField(blank= True,null=True)
    # end_time = models.TimeField(blank= True,null=True)

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

    likes = models.ManyToManyField(User, related_name = "likes", blank= True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    bookmark =models.ManyToManyField(User,related_name='bookmarks',blank=True,default=None)

    updated_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects =models.Manager()
    publishedEvents = PublishedEventsManager()

    def __str__(self):
        return self.name


def pre_save_event_id(sender,instance,*args, **kwargs):
    if not instance.event_id:
        instance.event_id =unique_event_id_generation(instance)
pre_save.connect(pre_save_event_id,sender=Event)

# def get_absolute_url(self):
#     return reverse("event-detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    event =models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    content =models.TextField(max_length=255)
    parent = models.ForeignKey("self", null=True,blank=True, on_delete=models.CASCADE)
    is_active =models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-created_at',)

    def __str__(self):
        return  self.user.username 
    def children(self):
        return Comment.filter(parent=self)
    @property 
    def is_parent(self):
        if self.parent is not None:
           return False
        return True

