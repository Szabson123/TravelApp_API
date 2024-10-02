from django.shortcuts import render

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema
from .serializers import UserSerializer
from .models import CustomUser


class RegisterView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        request={
            'type': 'object',
            'properties': {
                'refresh': {'type': 'string', 'description': 'Refresh token'}
            },
            'required': ['refresh']
        },
        responses={205: 'Token successfully blacklisted', 400: 'Invalid request'}
    )
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response("There is no token", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)