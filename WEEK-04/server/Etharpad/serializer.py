from rest_framework import serializers
from .models import EtharpadClass

class EtharpadClassSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = EtharpadClass
        fields = '__all__'