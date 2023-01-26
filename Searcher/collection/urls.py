from django.urls import path
from . import views

urlpatterns = [
    path('', views.response_map),
    path('help/', views.response_help, name="Help")
]
