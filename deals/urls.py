from django.urls import path
from . import views

urlpatterns = [
    path('scan/start', views.start_scan, name='start_scan'),
    path('scan/<str:scan_id>/results', views.get_scan_results, name='get_scan_results'),
]
