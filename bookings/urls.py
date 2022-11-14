from django.urls import path ,include

from rest_framework_nested import routers
from  events.views import EventsViewset
from . views import BookingViewsets,Search,MyBookings

from rest_framework.routers import DefaultRouter


router = routers.SimpleRouter()
user_router =routers.DefaultRouter()

user_router.register(r'user_bookings',MyBookings)
router.register(r'events',EventsViewset,basename="event")
events_router = routers.NestedDefaultRouter(router,r'events',lookup='event')

events_router.register(r'bookings',BookingViewsets,basename="booking")

# router.register('(?P<tag__slug>[^/.]+)', EventsViewset)

urlpatterns = [
    path(r'',include(user_router.urls)),
    path(r'',include(events_router.urls)),
#    path('tags/<slug>/',EventsTags.as_view()),
#    path('user-events/<int:user_id>/',UserEvents.as_view()),
#    path('events/my-events/<username>/',MyEvents.as_view()),
#    path('events/event-tags/<slug>/',EventByTag.as_view()),
   path('search/',Search,name='search'),
#    path('events/like_unlike/<int:event_id>',LikeView.as_view()),
#    path('events/bookmark/<int:event_id>',AddBookmark.as_view())
]   
# urlpatterns += router.urls

# {% url 'events:detail' %}
