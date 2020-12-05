from django.contrib import admin
from django.urls import path, include
from item import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')),
    url(r'^export-csv/$', views.export, name='export'),
]

