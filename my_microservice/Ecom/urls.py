#Ecom urls.py

from django.urls import path 
from .views import health_check

urlpatterns = [
    
    path('healthCheck/', health_check),
]
