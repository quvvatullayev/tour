from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    News,
)
from ..serializers import (
    NewsSerializer,
)

class NewsCreate(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = NewsSerializer(data=data)
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
    
class NewsList(APIView):
    def get(self, request:Request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NewsDetail(APIView):
    def get(self, request:Request, id):
        news = News.objects.get(id=id)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NewsUpdate(APIView):
    def post(self, request:Request, id):
        data = request.data
        news = News.objects.get(id=id)
        news.name = data.get('name', news.name)
        news.discription = data.get('discription', news.discription)
        news.created = data.get('created', news.created)
        news.img = data.get('img', news.img)
        news.appeal = data.get('appeal', news.appeal)
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NewsDelete(APIView):
    def post(self, request:Request, id):
        news = News.objects.get(id=id)
        news.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    