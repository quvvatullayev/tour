from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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
    @swagger_auto_schema(
            operation_description="Get Home",
            responses={
                200: openapi.Response(
                description="Successful response",
                content={'application/json': {
                    'example': {
                        'countries': [
                            {
                                'id': 1,
                                'name': 'Uzbekistan',
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'youtube_url': 'https://www.youtube.com/embed/5qap5aO4i9A',
                                'img': 'http://'
                            }
                        ],
                        'exclusives': [
                            {
                                'id': 1,
                                'name': 'Uzbekistan',
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'youtube_url': 'https://www.youtube.com/embed/5qap5aO4i9A',
                                'img': 'http://'
                            }
                        ],
                        'about_companies': [
                            {
                                'id': 1,
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'img': 'http://'
                            }
                        ],
                        'news': [
                            {
                                'id': 1,
                                'title': 'Uzbekistan',
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'img': 'http://'
                            }
                        ],
                        'commits': [
                            {
                                'id': 1,
                                'name': 'Uzbekistan',
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'img': 'http://'
                            }
                        ],
                        'contacts': [
                            {
                                'id': 1,
                                'name': 'Uzbekistan',
                                'discription': 'Uzbekistan is a country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south and Turkmenistan to the south-west. Along with Liechtenstein, it is one of the world\'s only two doubly landlocked countries.',
                                'img': 'http://'
                            }
                        ],
                    }
                }
                }
            ),
            }
            )
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