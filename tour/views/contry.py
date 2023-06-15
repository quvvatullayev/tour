from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Country,
)
from ..serializers import (
    CountrySerializer,
)

class CountryCreate(APIView):
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
    def get(self, request:Request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CountryDetail(APIView):
    def get(self, request:Request, id):
        country = Country.objects.get(id=id)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CountryUpdate(APIView):
    def put(self, request:Request, id):
        country = Country.objects.get(id=id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                'error': serializer.errors,
                'message': 'Invalid data'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CountryDelete(APIView):
    def delete(self, request:Request, id):
        country = Country.objects.get(id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)