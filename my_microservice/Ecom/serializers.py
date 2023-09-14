
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from .models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 