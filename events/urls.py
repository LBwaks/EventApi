from django.urls import path 
from . views import EventsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'events',EventsViewset)

urlpatterns = [
    
]
urlpatterns += router.urls


