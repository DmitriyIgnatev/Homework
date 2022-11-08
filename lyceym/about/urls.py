from django.urls import path
from about import views


urlpatterns = [
    path('about/', views.description, name='about'),
    path('ab/', views.description_new, name='ab')
]
