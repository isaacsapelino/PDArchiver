from django.urls import path, re_path

from . import views

urlpatterns = [
    path('home/', views.homePage.as_view(), name='home'),
]
