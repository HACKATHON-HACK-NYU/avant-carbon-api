from abc import ABC

from rest_framework import serializers
from .models import Card

class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'