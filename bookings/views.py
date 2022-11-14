from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from events.permissions import OwnerToEditOrDelete
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class BookingViewsets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class =BookingSerializer
    permission_classes =[IsAuthenticated,OwnerToEditOrDelete]
    lookup_field ='uuid'
    def perform_create(self, serializer):
        return super().perform_create(serializer.save(
            user=self.request.user,
            event_id = 2))
    # @action(detail=False ,methods=['get'],url_path='my_bookings',permission_classes=[IsAuthenticated])
    # def MyBooking(self,request,username = None):
    #     user =self.request.user
    #     queryset = self.get_queryset().filter(user = user)
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page,many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset,many =True)
          
    
    
class MyBookings(mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):    
    queryset = Booking.objects.all()
    serializer_class =BookingSerializer 
    
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(user=user)
    
    # def list(self,request):
    #     user =self.request.user
    #     queryset = Booking.objects.filter(user = user)
    #     # page = self.paginate_queryset(queryset)
    #     # if page is not None:
    #     #     serializer = self.get_serializer(page,many=True)
    #     #     return self.get_paginated_response(serializer.data)
    #     serializer = BookingSerializer(queryset,many =True)
    #     return Response(serializer.data)  
    
    # def retrieve(self,request, pk=None):
    #     user = self.request.user
    #     queryset = Booking.objects.filter(user = user)
    #     booking = get_object_or_404(queryset,uuid=pk)
    #     serializer = BookingSerializer(booking)
    #     return Response(serializer.data)
    
    # def update(self, request, pk=None):
    #     pass
    
    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     user = self.request.user
    #     queryset = Booking.objects.filter(user=user)
    #     booking = get_object_or_404(queryset ,uuid=pk)
    #     booking.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
def Search(request):
    pass


# def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if request.user.id == request.data['author']:
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#         else:
#             return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED
            