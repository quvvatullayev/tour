from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Exclusive,
    Contact,
)
from ..serializers import (
    ExclusiveSerializer,
    ContactSerializer,
)

class ExclusiveCreate(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = ExclusiveSerializer(data=data)
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
    
class ExclusiveList(APIView):
    def get(self, request:Request):
        exclusives = Exclusive.objects.all()
        serializer = ExclusiveSerializer(exclusives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ExclusiveDetail(APIView):
    def get(self, request:Request, id):
        exclusive = Exclusive.objects.get(id=id)
        exclusives = Exclusive.objects.all()
        contacts = Contact.objects.all()
        serializer = ExclusiveSerializer(exclusive)
        serializers = ExclusiveSerializer(exclusives, many=True)
        contact_serializer = ContactSerializer(contacts, many=True)
        return Response(
            {
                'exclusive': serializer.data,
                'exclusives': serializers.data,
                'contacts': contact_serializer.data,
            },
            status=status.HTTP_200_OK
        )
    
class ExclusiveUpdate(APIView):
    def post(self, request:Request, id):
        data = request.data
        exclusive = Exclusive.objects.get(id=id)
        exclusive.name = data.get('name', exclusive.name)
        exclusive.price = data.get('price', exclusive.price)
        exclusive.duration = data.get('duration', exclusive.duration)
        exclusive.save()
        serializer = ExclusiveSerializer(exclusive)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ExclusiveDelete(APIView):
    def post(self, request:Request, id):
        exclusive = Exclusive.objects.get(id=id)
        exclusive.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)