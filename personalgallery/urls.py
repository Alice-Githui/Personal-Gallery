from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#app urls 
urlpatterns=[
    path('', views.index, name="indexpage"),
    path('search/', views.show_category, name="search_categories")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)