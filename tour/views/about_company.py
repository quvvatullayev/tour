from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    About_company,
)
from ..serializers import (
    About_companySerializer,
)

class About_companyCreate(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = About_companySerializer(data=data)
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
    
class About_companyList(APIView):
    def get(self, request:Request):
        about_companys = About_company.objects.all()
        serializer = About_companySerializer(about_companys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class About_companyDetail(APIView):
    def get(self, request:Request, id):
        about_company = About_company.objects.get(id=id)
        serializer = About_companySerializer(about_company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class About_companyUpdate(APIView):
    def post(self, request:Request, id):
        data = request.data
        about_company = About_company.objects.get(id=id)
        about_company.discription = data.get('discription', about_company.discription)
        about_company.img = data.get('img', about_company.img)
        about_company.save()
        serializer = About_companySerializer(about_company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class About_companyDelete(APIView):
    def post(self, request:Request, id):
        about_company = About_company.objects.get(id=id)
        about_company.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    

    