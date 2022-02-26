from abc import ABC

from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
        
class UserAccountSerializers_1(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        depth = 1
        fields = ('id','email','first_name','last_name','username')

