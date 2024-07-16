# booking/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminAPI(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('X-API-Key') == 'your_secret_api_key'
