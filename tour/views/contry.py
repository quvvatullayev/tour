from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Country,
)
from ..serializers import (
    CountrySerializer,
)

class CountryCreate(APIView):
    @swagger_auto_schema(operation_description="Create Country", request_body=CountrySerializer)
    def post(self, request:Request):
        data = request.data
        serializer = CountrySerializer(data=data)
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
    
class CountryList(APIView):
    @swagger_auto_schema(operation_description="Get Country list")
    def get(self, request:Request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CountryDetail(APIView):
    @swagger_auto_schema(operation_description="Get Country detail")
    def get(self, request:Request, id):
        country = Country.objects.get(id=id)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CountryUpdate(APIView):
    @swagger_auto_schema(operation_description="Update Country", request_body=CountrySerializer)
    def post(self, request:Request, id):
        data = request.data
        country = Country.objects.get(id=id)
        country.name = data.get('name', country.name)
        country.discription = data.get('discription', country.discription)
        country.youtube_url = data.get('youtube_url', country.youtube_url)
        country.save()
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
class CountryDelete(APIView):
    @swagger_auto_schema(operation_description="Delete Country", request_body=CountrySerializer)
    def post(self, request:Request, id):
        country = Country.objects.get(id=id)
        country.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)