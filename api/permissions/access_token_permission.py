from rest_framework import permissions
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
import pdb
from api.models import User

class IsValidAccessToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token_type, access_token = request.headers.get('Authorization').split()
        user = User.objects.get(username=request.user.username)
        outstanding_token = OutstandingToken.objects.filter(token=access_token, user=user).last()
        if BlacklistedToken.objects.filter(token=outstanding_token).exists():
            return False
        return True
