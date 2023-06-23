from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from ..models import (
#     User_model,
# )
from ..serializers import (
    UserSerializer,
)

class CreateUser(APIView):
    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserSerializer,
        responses={200: UserSerializer}
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
        request_body=UserSerializer,
        responses={200: UserSerializer}
    )
    def post(self, request: Request) -> Response:
        user = request.user
        if user:
            # check token
            user_token = Token.objects.get_or_create(user=user)
            return Response({"token": user_token[0].key})

        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
