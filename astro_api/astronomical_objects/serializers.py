from rest_framework import serializers
from .models import NotStarObject, StarObject


class StarListSerializer(serializers.ModelSerializer):
    """
    Сериализатор списка звёзд
    """

    class Meta:
        model = StarObject
        fields = '__all__'


class NotStarListSerializer(serializers.ModelSerializer):
    """
    Сериализатор списка не звёзд
    """

    class Meta:
        model = NotStarObject
        fields = '__all__'
