from django.urls import path
from rest_framework import views
from . import view_api

urlpatterns=[ 
    path('login/',view_api.login_api.as_view(),name='login-page'),
    path('register/',view_api.register_api.as_view())
]