from rest_framework import permissions

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsLibrarianOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

