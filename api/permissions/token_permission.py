from rest_framework import permissions
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

class DenyBlacklistedToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token_type, access_token = request.headers.get('Authorization').split()
        if BlacklistedToken.objects.filter(token=access_token).exists():
            return False
        return True
