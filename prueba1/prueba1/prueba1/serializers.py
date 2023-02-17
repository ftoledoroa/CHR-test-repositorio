from rest_framework import serializers
from .models import Estaciones

class EstacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estaciones
        fields = '__all__'
