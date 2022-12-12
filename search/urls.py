from django.urls import path, re_path


from . import views

urlpatterns = [
    path('home/', views.homePage.as_view(), name='search'),
    path('upload/', views.uploadPage.as_view(), name='upload'),
    path('abstract/<str:slug>', views.abstractPage.as_view(), name='abstract'),
    path('abstract/<str:slug>/<str:filename>', views.DownloadFile.as_view(), name='downloadFile'),
]


