from rest_framework.serializers import ModelSerializer
from .models import productDetails


class ProductDetailsSerializer(ModelSerializer):
    class Meta:
        model = productDetails
        fields = '__all__'