from django.urls import path
from . import views

urlpatterns = [
    path('', views.response_map),
    path('base/', views.responseBase)
]
