from django.urls import path 
from . views import EventsViewset,MyEvents,TagsViewSet,AddBookmark,CommentsViewset,Search,UserEvents,EventByTag,LikeView,EventsViewset
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register(r'events',EventsViewset,basename="event")
router.register(r'tags',TagsViewSet,basename='tag')
router.register(r'comments',CommentsViewset,basename='comment')

# router.register('(?P<tag__slug>[^/.]+)', EventsViewset)

urlpatterns = [
#    path('tags/<slug>/',EventsTags.as_view()),
   path('user-events/<int:user_id>/',UserEvents.as_view()),
#    path('events/my-events/<username>/',MyEvents.as_view()),
   path('events/event-tags/<slug>/',EventByTag.as_view()),
   path('search/',Search.as_view(),name='search'),
   path('events/like_unlike/<int:event_id>',LikeView.as_view()),
   path('events/bookmark/<int:event_id>',AddBookmark.as_view())
]   
urlpatterns += router.urls

# {% url 'events:detail' %}
