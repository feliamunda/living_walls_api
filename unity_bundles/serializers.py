from django.db.models import fields
from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    bundle = serializers.FileField()

    class Meta:
        model = Asset

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)