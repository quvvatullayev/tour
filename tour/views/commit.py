from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Commit,
)
from ..serializers import (
    CommitSerializer,
)

class CommitCreate(APIView):
    @swagger_auto_schema(operation_description="Create Commit")
    def post(self, request:Request):
        data = request.data
        serializer = CommitSerializer(data=data)
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
    
class CommitList(APIView):
    @swagger_auto_schema(operation_description="Get Commit list")
    def get(self, request:Request):
        commits = Commit.objects.all()
        serializer = CommitSerializer(commits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommitDetail(APIView):
    @swagger_auto_schema(operation_description="Get Commit detail")
    def get(self, request:Request, id):
        commit = Commit.objects.get(id=id)
        serializer = CommitSerializer(commit)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommitUpdate(APIView):
    @swagger_auto_schema(operation_description="Update Commit")
    def post(self, request:Request, id):
        data = request.data
        commit = Commit.objects.get(id=id)
        commit.name = data.get('name', commit.name)
        commit.discription = data.get('discription', commit.discription)
        commit.save()
        serializer = CommitSerializer(commit)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommitDelete(APIView):
    @swagger_auto_schema(operation_description="Delete Commit")
    def post(self, request:Request, id):
        commit = Commit.objects.get(id=id)
        commit.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)