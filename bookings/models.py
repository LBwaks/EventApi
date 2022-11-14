from asyncio import events
from email.policy import default
from django.db import models
from django.conf import settings
from events.models import Event
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
import random ,string
from django.urls import reverse
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField
import uuid

# Create your models here.
User = settings.AUTH_USER_MODEL

class Booking(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, related_name='user_bookings', on_delete=models.CASCADE,null=False)
    event =  models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE,null=False)
    tickets = models.IntegerField(_("Number of Tickets"))
    status = models.CharField(max_length=25,default='UNPAID')
    updated_at = models.DateTimeField(auto_now=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name