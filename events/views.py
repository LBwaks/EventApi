from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,TagSerializer,CategorySerializer,EventSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Event,Tag,Category



# Create your views here.
class EventsViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []