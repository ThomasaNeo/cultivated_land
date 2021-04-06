from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index', views.house_short),
    re_path('downloadfile/[1-9][0-9]', views.exporttoexcel),
]
