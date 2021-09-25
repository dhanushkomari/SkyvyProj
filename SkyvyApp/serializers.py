from django.db.models import fields
from rest_framework import serializers
from .models import BotModel

class BotDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = BotModel
        fields = ('x','y','angle', 'delivering')

