from django.urls import path
from .views import (
    HomeView,
)
from . import views

app_name = 'item'
urlpatterns = [
    path('', HomeView.as_view(), name='item-home'),
]

