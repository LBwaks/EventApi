from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event','user','tickets','status','updated_at','created_at')

admin.site.register(Booking,BookingAdmin)

