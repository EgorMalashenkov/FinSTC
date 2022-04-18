from rest_framework import permissions


class DealerPermission(permissions.BasePermission):
    message = "Editing cars is allowed only to dealers"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (obj.dealer == request.user) or (request.method in permissions.SAFE_METHODS):
            return True
        return False
