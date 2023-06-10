from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True

        elif bool(request.user and request.user.is_staff):
            return True