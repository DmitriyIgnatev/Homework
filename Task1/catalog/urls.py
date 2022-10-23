
from django.urls import path, re_path
from catalog import views


urlpatterns = [
    path('catalog/', views.item_list),
    re_path('catalog/(?P<pk>[0-9]+)', views.item_detail),
]
