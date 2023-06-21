from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    User,
)
from ..serializers import (
    UserSerializer,
)

class UserCreate(APIView):
    @swagger_auto_schema(operation_description="Create User", request_body=UserSerializer)
    def post(self, request:Request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                'error': serializer.errors,
                'message': 'Invalid data'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class UserList(APIView):
    @swagger_auto_schema(operation_description="Get User list")
    def get(self, request:Request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetail(APIView):
    @swagger_auto_schema(operation_description="Get User detail")
    def get(self, request:Request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserUpdate(APIView):
    @swagger_auto_schema(operation_description="Update User", request_body=UserSerializer)
    def post(self, request:Request, id):
        data = request.data
        user = User.objects.get(id=id)
        user.name = data.get('name', user.name)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.emile = data.get('emile', user.emile)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserDelete(APIView):
    @swagger_auto_schema(operation_description="Delete User", request_body=UserSerializer)
    def post(self, request:Request, id):
        user = User.objects.get(id=id)
        user.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    