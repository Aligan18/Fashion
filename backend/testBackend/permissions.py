from rest_framework import permissions

from clients.models import Clients


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return bool(request.user.is_superuser)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated):
            if bool(obj.user == request.user):
                return True


class IsOwnerForList(permissions.BasePermission):  # требует /?user=<id>
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            user = request.query_params.get('user')
            if user == request.user.id:
                return True


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            is_client = Clients.objects.filter(user=request.user).exists()
            if is_client:
                return True
