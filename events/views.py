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




# Create your views here.
class EventsViewset(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,OwnerToEditOrDelete]
    queryset = Event.publishedEvents.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(user=self.request.user))

# class EventsTags(generics.ListAPIView):
#     serializer_class = EventSerializer
#     queryset =Event.publishedEvents.all()

#     def get_queryset(self):
#         # events = Event.objects.filter()
#         queryset =super().get_queryset()
#         return queryset.filter(tag=1)
    