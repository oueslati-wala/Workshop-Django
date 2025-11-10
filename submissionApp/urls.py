from django.urls import path
from .views import (
    SubmissionListView,
    SubmissionDetailView,
    SubmissionCreateView,
    SubmissionUpdateView,
)

urlpatterns = [
    path('list/', SubmissionListView.as_view(), name='submission_list'),
    path('<str:pk>/', SubmissionDetailView.as_view(), name='submission_detail'),
    path('add/', SubmissionCreateView.as_view(), name='submission_add'),
    path('update/<str:pk>/', SubmissionUpdateView.as_view(), name='submission_update'),
]