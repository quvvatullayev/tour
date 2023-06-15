from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Appeal,
)
from ..serializers import (
    AppealSerializer,
)

class AppealCreate(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = AppealSerializer(data=data)
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
    
class AppealList(APIView):
    def get(self, request:Request):
        appeals = Appeal.objects.all()
        serializer = AppealSerializer(appeals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AppealDetail(APIView):
    def get(self, request:Request, id):
        appeal = Appeal.objects.get(id=id)
        serializer = AppealSerializer(appeal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AppealUpdate(APIView):
    def post(self, request:Request, id):
        data = request.data
        appeal = Appeal.objects.get(id=id)
        appeal.name = data.get('name', appeal.name)
        appeal.phone_number = data.get('phone_number', appeal.phone_number)
        appeal.emile = data.get('emile', appeal.emile)
        appeal.message = data.get('message', appeal.message)
        appeal.title = data.get('title', appeal.title)
        appeal.save()
        serializer = AppealSerializer(appeal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AppealDelete(APIView):
    def post(self, request:Request, id):
        appeal = Appeal.objects.get(id=id)
        appeal.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    