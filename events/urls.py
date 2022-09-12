from django.urls import path 
from . views import EventsViewset,MyEvents,Search,UserEvents,EventByTag
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'events',EventsViewset,basename="event")

urlpatterns = [
    # path('tags/<pk>/',EventsTags.as_view())
   path('user-events/<int:user_id>/',UserEvents.as_view()),
   path('events/my-events/<username>/',MyEvents.as_view()),
   path('event-tags/<int:tag_id>/',EventByTag.as_view()),
   path('search/',Search.as_view(),name='search')
]   
urlpatterns += router.urls

# {% url 'events:detail' %}
