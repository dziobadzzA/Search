from django.urls import path
from . import views

urlpatterns = [
    path('', views.responseMap),
    path('base/', views.responseBase)
]
