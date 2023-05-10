from api.serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from api.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from api.permissions import IgnoreBlacklistPermission
from rest_framework_simplejwt.exceptions import TokenError
from datetime import datetime
import uuid

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            user = self.get_user(request.data.get('username'))
            user.device_id = request.data.get('device_id')
            user.device_type = request.data.get('device_type')
            user.time_zone = request.data.get('time_zone')
            user.save()
        return response
    
    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password.')
        return user

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IgnoreBlacklistPermission)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token_type, access_token = request.headers.get('Authorization').split()
            jti = uuid.uuid4().hex
            user = User.objects.get(username=request.user.username)
            expires_at = datetime.now()
            outstanding_token = OutstandingToken.objects.create(token=access_token, user=user, jti=jti, expires_at=expires_at)
            blacklisted_token = BlacklistedToken.objects.create(token=outstanding_token)
            token.blacklist()
            user.device_id = "None"
            user.device_type = "None"
            user.time_zone = "None"
            user.save()
            return Response({'message': "Logout Successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({'message': 'Refresh Token is invalid or expired'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
