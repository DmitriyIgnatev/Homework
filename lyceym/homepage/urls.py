from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('home', views.home_new)
]
