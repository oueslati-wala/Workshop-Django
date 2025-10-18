from django.urls import path
from .views import *
urlpatterns =[
    path("liste/",ConferenceList.as_view(),name="liste_conferences"),
    path("<int:pk>/",ConferenceDetails.as_view(),name="conference_details"),
    path("add/",ConferenceCreate.as_view(),name="conference_add"),
    path("update/<int:pk>/", ConferenceUpdate.as_view(), name="update_conference"),
    path("delete/<int:pk>/", ConferenceDelete.as_view(), name="delete_conference")
]