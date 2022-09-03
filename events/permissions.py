from email import message
from rest_framework import permissions

class OwnerToEditOrDelete(permissions.BasePermission):
    message = 'Only Owners to edit or delete !'

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #       return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user :
            return True
        return False