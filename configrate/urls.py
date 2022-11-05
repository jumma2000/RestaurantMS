from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('user/',views.get_use,name="user"),
]