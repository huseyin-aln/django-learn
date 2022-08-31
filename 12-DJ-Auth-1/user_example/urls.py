from django.urls import path, include
from .views import (
    home,
    special,
    register
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path('register/', register, name="register"),
]
