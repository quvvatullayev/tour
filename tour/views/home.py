from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Country,
    Exclusive,
    About_company,
    News,
    Commit,
    Appeal,
    Contact,
    User,
)
from ..serializers import (
    CountrySerializer,
    ExclusiveSerializer,
    About_companySerializer,
    NewsSerializer,
    CommitSerializer,
    AppealSerializer,
    ContactSerializer,
    UserSerializer,
)

class HomeViews(APIView):
    @swagger_auto_schema(operation_description="Get Home")
    def get(self, request:Request):
        countries = Country.objects.all()
        exclusives = Exclusive.objects.all()
        about_companies = About_company.objects.all()
        news = News.objects.all()
        commits = Commit.objects.all()
        contacts = Contact.objects.all()
        countries_serializer = CountrySerializer(countries, many=True)
        exclusives_serializer = ExclusiveSerializer(exclusives, many=True)
        about_companies_serializer = About_companySerializer(about_companies, many=True)
        news_serializer = NewsSerializer(news, many=True)
        commits_serializer = CommitSerializer(commits, many=True)
        contacts_serializer = ContactSerializer(contacts, many=True)
        return Response(
            {
                'countries': countries_serializer.data,
                'exclusives': exclusives_serializer.data,
                'about_companies': about_companies_serializer.data,
                'news': news_serializer.data,
                'commits': commits_serializer.data,
                'contacts': contacts_serializer.data,
            },
            status=status.HTTP_200_OK
        )