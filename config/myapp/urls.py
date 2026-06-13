from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setSessionData/', views.setSessionData),
    path('getSeesionData/', views.getSeesionData),
    path('clearSpecificSession/', views.clearSpecificSession),
    path('getSeesionData/', views.getSeesionData)
]