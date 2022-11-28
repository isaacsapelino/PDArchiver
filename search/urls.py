from django.urls import path, re_path

from . import views

urlpatterns = [
    path('home/', views.homePage.as_view(), name='search'),
    path('upload/', views.uploadPage.as_view(), name='upload'),
]
