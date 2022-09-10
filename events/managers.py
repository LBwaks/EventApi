from datetime import datetime
from django.db import models
import datetime

class PublishedTagManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = True)

class PublishedCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = True)

class PublishedEventsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = True, start_date__gte= datetime.datetime.now())
