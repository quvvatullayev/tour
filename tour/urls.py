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

from .views.about_company import (
    About_companyCreate,
    About_companyList,
    About_companyDetail,
    About_companyUpdate,
    About_companyDelete,
)

urlpatterns += [
    path('about_company_list/', About_companyList.as_view()),
    path('about_company_create/', About_companyCreate.as_view()),
    path('about_company_detail/<int:id>/', About_companyDetail.as_view()),
    path('about_company_update/<int:id>/', About_companyUpdate.as_view()),
    path('about_company_delete/<int:id>/', About_companyDelete.as_view()),
]

from .views.appeal import (
    AppealCreate,
    AppealList,
    AppealDetail,
    AppealUpdate,
    AppealDelete,
)

urlpatterns += [
    path('appeal_list/', AppealList.as_view()),
    path('appeal_create/', AppealCreate.as_view()),
    path('appeal_detail/<int:id>/', AppealDetail.as_view()),
    path('appeal_update/<int:id>/', AppealUpdate.as_view()),
    path('appeal_delete/<int:id>/', AppealDelete.as_view()),
]



