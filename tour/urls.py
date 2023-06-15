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

from .views.commit import (
    CommitCreate,
    CommitList,
    CommitDetail,
    CommitUpdate,
    CommitDelete,
)

urlpatterns += [
    path('commit_list/', CommitList.as_view()),
    path('commit_create/', CommitCreate.as_view()),
    path('commit_detail/<int:id>/', CommitDetail.as_view()),
    path('commit_update/<int:id>/', CommitUpdate.as_view()),
    path('commit_delete/<int:id>/', CommitDelete.as_view()),
]

from .views.contact import (
    ContactCreate,
    ContactList,
    ContactDetail,
    ContactUpdate,
    ContactDelete,
)

urlpatterns += [
    path('contact_list/', ContactList.as_view()),
    path('contact_create/', ContactCreate.as_view()),
    path('contact_detail/<int:id>/', ContactDetail.as_view()),
    path('contact_update/<int:id>/', ContactUpdate.as_view()),
    path('contact_delete/<int:id>/', ContactDelete.as_view()),
]

from .views.exclusive import (
    ExclusiveCreate,
    ExclusiveList,
    ExclusiveDetail,
    ExclusiveUpdate,
    ExclusiveDelete,
)

urlpatterns += [
    path('exclusive_list/', ExclusiveList.as_view()),
    path('exclusive_create/', ExclusiveCreate.as_view()),
    path('exclusive_detail/<int:id>/', ExclusiveDetail.as_view()),
    path('exclusive_update/<int:id>/', ExclusiveUpdate.as_view()),
    path('exclusive_delete/<int:id>/', ExclusiveDelete.as_view()),
]


