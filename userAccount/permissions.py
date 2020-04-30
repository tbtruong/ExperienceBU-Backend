from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows Editing of a profile"""

    def has_object_permission(self, request, view, obj):
        """checks if user is trying to update own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
