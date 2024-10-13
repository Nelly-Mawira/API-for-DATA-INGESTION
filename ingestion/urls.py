from django.urls import path
from .views import DataUploadView, DataProcessView, DataStatusView, DataResultView




urlpatterns = [
    path('data/upload/', DataUploadView.as_view(), name='data-upload'),
    path('data/process/', DataProcessView.as_view(), name='data-process'),
    path('data/status/<int:data_id>/', DataStatusView.as_view(), name='data-status'),
    path('data/results/<int:data_id>/', DataResultView.as_view(), name='data-results'),

]

