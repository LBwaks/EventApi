from django.urls import path 
from . views import EventsViewset #,EventsTags
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'events',EventsViewset,basename="event")

urlpatterns = [
    # path('tags/<pk>/',EventsTags.as_view())
]
urlpatterns += router.urls

# {% url 'events:detail' %}
