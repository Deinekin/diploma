from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Permission for user-owners"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser


class IsSeller(BasePermission):
    """Permission for sellers and superusers"""

    def has_object_permission(self, request, view, obj):
        return request.user.is_seller or request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_seller or request.user.is_superuser
