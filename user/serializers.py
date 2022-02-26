from abc import ABC

from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'