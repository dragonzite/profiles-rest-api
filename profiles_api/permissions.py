from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile

    Keyword arguments: none, base
    argument -- description
    Return: return_description
    """

    def has_object_permissions(self, request, view, obj):
        """Check user is trying to edit their own profile

        Args:
            request (info): requset informetion
            view (obj): the view
            obj (obj): the object
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id