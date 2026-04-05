"""
Custom permissions for the API
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the object.
        return obj.id == request.user.id


class IsEmailVerified(permissions.BasePermission):
    """
    Custom permission to only allow users with verified emails.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_email_verified
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_email_verified


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to write, others can only read.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff