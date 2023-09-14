#Ecom urls.py

from django.urls import path
from .views import HealthCheck, ProductCreateView, ProductListview, ProductListCreateView, ProductRetrieveUpdateDestroyView, ProductDestroyView


urlpatterns = [
    path('', HealthCheck, name='HealthCheck'),
    path('products/', ProductListview.as_view(), name='product-list-filter'),   
    path('products/new', ProductCreateView.as_view(), name='product-create'),   
    path('products/<int:pk>/delete', ProductDestroyView.as_view(), name='product-delete'),  
     
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),    
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    
]