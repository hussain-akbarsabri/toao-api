from rest_framework import permissions
from api.models import BlackListedAccessToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
import pdb
from api.models import User

class IgnoreBlacklistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token_type, access_token = request.headers.get('Authorization').split()
        user = User.objects.get(username=request.user.username)
        out_token = OutstandingToken.objects.filter(token=access_token, user=user).last()
        if BlacklistedToken.objects.filter(token=out_token).exists():
            return False
        return True
