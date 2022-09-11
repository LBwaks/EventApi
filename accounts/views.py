from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.auth import AuthToken
from .serializers import UserSerializer
from events.serializers import EventSerializer
from events.models import Event
from rest_framework import viewsets
from django.contrib.auth.models import User
from allauth.account.views import ConfirmEmailView
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from rest_framework import generics
# Create your views here.

# @api_view(['POST',])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']

#     _,token =AuthToken.objects.create(user)

class UserViewset(viewsets.ModelViewSet):
    serializer_class =UserSerializer
    queryset = User.objects.all()


    
    
class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        user = get_user_model().objects.get(email=self.object.email_address.email)
        redirect_url = reverse('user', args=(user.id,))
        return redirect(redirect_url)





    
