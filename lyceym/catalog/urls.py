from django.urls import path, re_path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.item_list),
    re_path(r'(?P<pk>^[1-9]\d*)/$', views.item_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
