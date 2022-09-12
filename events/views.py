from re import search
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import EventSerializer##UserSerializer,TagSerializer,CategorySerializer,
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Event,Tag,Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import OwnerToEditOrDelete
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
from .filters import EventFilter


# Create your views here.
class EventsViewset(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,OwnerToEditOrDelete]
    queryset = Event.publishedEvents.all()
    serializer_class = EventSerializer
    filter_backends =[DjangoFilterBackend]
    # filterset_fields =['tag','type','start_date','charge','venue']
    # search_fields=['^name']
    filterset_class =EventFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(user=self.request.user))


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
        return queryset.filter(tag_id = self.kwargs['tag_id'])
    