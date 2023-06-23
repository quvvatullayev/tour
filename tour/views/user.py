from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_yasg import openapi
from ..serializers import (
    UserSerializer,
)

class CreateUser(APIView):
    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={200: openapi.Response(
            description="Successful response",
            content={'application/json': {
                'example': {
                    'token': 'f7a2a3e0a4f0b0d6c2e6d2b8a1b7f6d2b8a1b7f6'
                }
            }}
        )
        }
    )
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_token = Token.objects.create(user=serializer.instance)
            return Response({"token": user_token.key})
        return Response(serializer.errors)
    
class LoginUser(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                # basic auth
                'basic': {
                    'type': openapi.TYPE_OBJECT,
                    'properties': {
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'password': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                }

            }
        ),
        responses={200: openapi.Response(
            description="Successful response",
            content={'application/json': {
                'example': {
                    'token': 'f7a2a3e0a4f0b0d6c2e6d2b8a1b7f6d2b8a1b7f6'
                }
            }}
        )

    }
    )
    def post(self, request: Request) -> Response:
        user = request.user
        if user:
            # check token
            user_token = Token.objects.get_or_create(user=user)
            return Response({"token": user_token[0].key})

        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
class LogoutUser(APIView):
    # cheak token
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Logout user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING),

            }
        ),
        responses={200: openapi.Response(
        description="Successful response",
        content={'application/json': {
            'example': {
                'message': 'User logout'
            }
        }}
        )}
    )
    def post(self, request: Request) -> Response:
        user = request.user
        if user:
            # get token
            user_token = Token.objects.get(user=user)
            user_token.delete()
            return Response({"message": "User logout"})
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
