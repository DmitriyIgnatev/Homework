
from django.urls import path
from homepage import views

urlpatterns = [
    path('home/', views.home),
]