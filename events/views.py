from re import search
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, EventSerializer, TagSerializer##UserSerializer,TagSerializer,CategorySerializer,
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event,Tag,Category,Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import OwnerToEditOrDelete
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
from .filters import EventFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.decorators import action


# Create your views here.
class MultipleFieldLookupMixin():
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class EventsViewset(viewsets.ModelViewSet):
    queryset = Tag.publishedTags.all()
    serializer_class = TagSerializer

    
class EventsViewset(viewsets.ModelViewSet):
    # @method_decorator(cache_page(60*60*2))
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,OwnerToEditOrDelete]
    queryset = Event.publishedEvents.all()
    serializer_class = EventSerializer
    filter_backends =[DjangoFilterBackend]
    lookup_field = 'slug'
    # filterset_fields =['tag','type','start_date','charge','venue']
    # search_fields=['^name']
    filterset_class =EventFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(user=self.request.user))
    def multiple_images(self,request, *args, **kwargs):
        serializer = MultipleImageSerializer(data = request.data or None)
        serializer.is_valid(raise_execption=True)
        images = serializer.validated_data.get('images')
        files_list = []
        for file in images :
            files_list.append(EventImage(images=file))
        if files_list:
            EventImage.objects.bulk_create(files_lis-0)

   
    @action(detail=False,methods=['get'],url_path='my_events',permission_classes=[IsAuthenticated])
    def my_events(self,request, username =None):
        user = self.request.user
        queryset =self.get_queryset().filter(user = user)
        page =self.paginate_queryset(queryset)
        if page is not None:
            serializer=self.get_serializer(page ,many =True)
            return self.get_paginated_response(serializer.data)
        serializer =self.get_serializer(queryset,many=True)      
        
        return Response(serializer.data)

    @action(detail=False,methods=['get'],url_path='user_event',permission_classes=[IsAuthenticatedOrReadOnly])
    def this_user_events(self,request,username = None):
        user = get_object_or_404(User,username=username)
        user_id =user.id
        queryset =self.get_queryset().filter(user_id = user_id)
        serializer =self.get_serializer(queryset,many =True)
        return Response(serializer.data)

    # @action(detail =False,methods=['post'],url_path='bookmark',permission_classes=[IsAuthenticatedOrReadOnly])
    # def bookmark(self,request,slug=None):
    #     queryset = queryset.bookmark.filter(id = self.request.id).exists()  
    #     pass
    @action(detail=False,methods=['get','post','put'],url_path='likingg/(?P<event_id>[^/.]+)' ,permission_classes =[IsAuthenticated])
    def likeUnlike(self,request,event_id=None):
        event = get_object_or_404(Event,id=event_id)
        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)
        return Response()

    @action(detail=False,methods=['get'],url_path='user_bookmark',permission_classes=[IsAuthenticated])
    def userBookmarks(self,request,username=None):
        user = self.request.user
        queryset = self.get_queryset().filter(bookmark = user)
        page =self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many = True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)

class CommentsViewset(viewsets.ModelViewSet):
    serializer_class =CommentSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(user=self.request.user))

class LikeView(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,event_id):
        event = get_object_or_404(Event,id = event_id)
        if event.likes.filter(pk =request.user.pk).exists():
            event.likes.remove(request.user)

        else :
            event.likes.add(request.user)
        return Response()
class AddBookmark(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,event_id):
        event = get_object_or_404(Event,id = event_id)
        if event.bookmark.filter(pk=request.user.pk).exists():
            event.bookmark.remove(request.user)
        else:
            event.bookmark.add(request.user)
        return Response()

class Search(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,OwnerToEditOrDelete]
    queryset = Event.publishedEvents.all()
    serializer_class = EventSerializer
    filter_backends =[filters.SearchFilter]
    search_fields=['^name','venue']

# class EventsTags(generics.ListAPIView):
#     serializer_class = EventSerializer
#     queryset =Event.publishedEvents.all()

#     def get_queryset(self):
#         # events = Event.objects.filter()
#         queryset =super().get_queryset()
#         return queryset.filter(tag=1)

class UserEvents(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Event.publishedEvents.filter(user_id=user_id)

class MyEvents(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset =Event.objects.all()
        username = self.request.query_params.get('username',None)
        if username is not None:
            queryset = queryset.filter(user = username)
        
        return queryset


class EventByTag(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset =Event.objects.all()
    # lookup_field ='slug'
    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug')
    #     tag = get_object_or_404(Tag,slug=slug)
    #     # events =Event.objects.filter(tag = tags)
    #     return Event.publishedEvents.filter(tag = tag)
    def get_queryset(self):
        queryset =super().get_queryset()
        return queryset.filter(slug = self.kwargs['slug'])

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.publishedTags.all()
    serializer_class = TagSerializer
