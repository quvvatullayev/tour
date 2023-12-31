from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Contact,
)
from ..serializers import (
    ContactSerializer,
)

class ContactCreate(APIView):
    @swagger_auto_schema(operation_description="Create Contact", request_body=ContactSerializer)
    def post(self, request:Request):
        data = request.data
        serializer = ContactSerializer(data=data)
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
    
class ContactList(APIView):
    @swagger_auto_schema(
        operation_description="Get Contact list",
        responses={200: ContactSerializer(many=True)}
        )
    def get(self, request:Request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContactDetail(APIView):
    @swagger_auto_schema(
            operation_description="Get Contact detail",
            responses={200: ContactSerializer()}
            )
    def get(self, request:Request, id):
        contact = Contact.objects.get(id=id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContactUpdate(APIView):
    @swagger_auto_schema(operation_description="Update Contact", request_body=ContactSerializer)
    def post(self, request:Request, id):
        data = request.data
        contact = Contact.objects.get(id=id)
        contact.area = data.get('area', contact.area)
        contact.phone_number = data.get('phone_number', contact.phone_number)
        contact.emile = data.get('emile', contact.emile)
        contact.location = data.get('location', contact.location)
        contact.telegram = data.get('telegram', contact.telegram)
        contact.instagram = data.get('instagram', contact.instagram)
        contact.facebook = data.get('facebook', contact.facebook)
        contact.save()
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContactDelete(APIView):
    @swagger_auto_schema(operation_description="Delete Contact", request_body=ContactSerializer)
    def post(self, request:Request, id):
        contact = Contact.objects.get(id=id)
        contact.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)