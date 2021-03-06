from rest_framework import permissions


class IsCreatedByOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.created_by == request.user)
        return obj.created_by == request.user
