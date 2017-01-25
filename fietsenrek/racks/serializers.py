from rest_framework import serializers

from . import models


class RackSerializer(serializers.ModelSerializer):
    place_id = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = models.Rack
        fields = '__all__'
