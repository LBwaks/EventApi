from rest_framework import permissions


class OwnerToEdit(permissions.BasePermission):
    message ='Only owners to edit or delete '
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user  :
            return True
        return False