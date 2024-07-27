from rest_framework import serializers
from .models import ProductsList

class ProductsListSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = ProductsList
        fields = '__all__'
        
class ProductsListOneSerializer(serializers.ModelSerializer):
 
    property = ProductsListSerializer(many=True)
 
    class Meta:
        model = ProductsList
        fields = "__all__"