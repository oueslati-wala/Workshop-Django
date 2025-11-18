from django.urls import path, re_path
from .views import (
    SubmissionListView,
    SubmissionDetailView,
    SubmissionCreateView,
    SubmissionUpdateView,
)

urlpatterns = [
    path('list/', SubmissionListView.as_view(), name='submission_list'),
    path('add/', SubmissionCreateView.as_view(), name='submission_add'),
    re_path(r'^(?P<pk>SUB-[A-F0-9]{8})/$', SubmissionDetailView.as_view(), name='submission_detail'),
    re_path(r"^update/(?P<pk>SUB-[A-F0-9]{8})/$", SubmissionUpdateView.as_view(), name="submission_update"),
]
