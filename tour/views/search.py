from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Exclusive,
)
from ..serializers import (
    ExclusiveSerializer,
)

class Search(APIView):
    @swagger_auto_schema(
            operation_description="Search",
            responses={200: ExclusiveSerializer(many=True)}
            )
    def get(self, request:Request):
        query = request.query_params.get('query')
        print(query, type(query))
        exclusives = Exclusive.objects.filter(name__contains=query)
        serializer = ExclusiveSerializer(exclusives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)