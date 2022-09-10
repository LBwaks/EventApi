from django.contrib import admin
from .models import Category,Tag,Event
from django.contrib.auth.models import User
# Register your models here.

class EventCategoryAdmin(admin.ModelAdmin):
    list_display= ('user','name','description','is_published','is_featured','created_date')
    prepopulated_fields = {"slug": ("name",)}
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user =request.user
        obj.save()
admin.site.register(Category,EventCategoryAdmin)


class TagEventAdmin(admin.ModelAdmin):
    list_display=  ('user','name','description','is_published','is_featured','created_date')
    prepopulated_fields ={'slug':('name',)}

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()
admin.site.register(Tag,TagEventAdmin)  


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id','name','tag','type','start_date','is_featured','is_published','created_date',)
    prepopulated_fields = {'slug':('name',)}
    # search_fields =('','','','','','','','','','','','','','','','','','','','','')
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()
admin.site.register(Event,EventAdmin)