from django.urls import path
from . import views



urlpatterns = [
     path('', views.index_view, name="index"),
     path('voluntary/', views.voluntary_view, name="voluntary"),
     path('supporter/', views.supporter_view, name="supporter"),
     ]