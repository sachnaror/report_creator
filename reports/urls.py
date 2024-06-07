from django.urls import path

from .views import ReportUploadFromPathView, ReportUploadView

urlpatterns = [
    path('upload/', ReportUploadView.as_view(), name='report-upload'),
    path('upload-from-path/', ReportUploadFromPathView.as_view(), name='report-upload-from-path'),
]
