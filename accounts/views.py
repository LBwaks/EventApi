from django.shortcuts import render
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerToEdit
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.auth import AuthToken
from .serializers import UserSerializer
from events.serializers import EventSerializer
from events.models import Event
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
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

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    parser_classes =[MultiPartParser,FormParser]
    permission_classes =[IsAuthenticated,OwnerToEdit]
    queryset =Profile.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        return  Profile.objects.filter(user = user_id)

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(user=self.request.user))

    # def retrieve(self, request, pk=None):
    #     user_id = self.request.user.id
    #     return  get_object_or_404(Profile , user = user_id)
        
    
   

class UserProfileViewset(viewsets.ModelViewSet):    
    serializer_class = ProfileSerializer
    parser_classes =[MultiPartParser,FormParser]
    # permission_classes[]
    def get_queryset(self):
        queryset = super().get_queryset()
        return  queryset.filter(user =self.kwargs['user_id'])
    
class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        user = get_user_model().objects.get(email=self.object.email_address.email)
        redirect_url = reverse('user', args=(user.id,))
        return redirect(redirect_url)





    
