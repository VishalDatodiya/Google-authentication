# authapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('google-auth/', views.google_authenticate, name='google-authenticate'),
]
