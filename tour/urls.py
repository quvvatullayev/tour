from django.urls import path
from .views.contry import (
    CountryCreate,
    CountryList,
    CountryDetail,
    CountryUpdate,
    CountryDelete,
)

urlpatterns = [
    path('country_list/', CountryList.as_view()),
    path('country_create/', CountryCreate.as_view()),
    path('country_detail/<int:id>/', CountryDetail.as_view()),
    path('country_update/<int:id>/', CountryUpdate.as_view()),
    path('country_delete/<int:id>/', CountryDelete.as_view()),
]