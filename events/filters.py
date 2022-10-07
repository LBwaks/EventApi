from django_filters.rest_framework import FilterSet
from .models import Event
class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields ={
            'tags':['exact'],
            'charge':['lt','gt'],
            'start_date':['exact','date__gt']
            
        } 