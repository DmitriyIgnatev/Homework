from django.urls import path, re_path
from catalog import views


urlpatterns = [
    path('', views.item_list, name='catalog'),
    re_path(r'(?P<pk>^[1-9]\d*)/$', views.item_detail, name='catalog_item'),
]
