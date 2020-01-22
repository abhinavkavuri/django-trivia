from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home-home"),
    path('about/', views.about, name="Home-about"),
    path('register_page/', views.register_page, name="Home-registerpage"),
]
