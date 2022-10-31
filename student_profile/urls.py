from django.urls import path
from .views import *
urlpatterns=[
    path('login',login),
    path('api/login/',login_api.as_view()),
    path('api/signup/',signUp.as_view()),
]