from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Exclusive,
)
from ..serializers import (
    ExclusiveSerializer,
)

class Search(APIView):
    def get(self, request:Request):
        query = request.query_params.get('query')
        print(query, type(query))
        exclusives = Exclusive.objects.filter(name__contains=query)
        print(exclusives)
        serializer = ExclusiveSerializer(exclusives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)