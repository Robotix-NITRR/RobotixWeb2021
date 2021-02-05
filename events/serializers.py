from rest_framework import serializers
from .models import Event,Workshop


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class WorkshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop
        fields = "__all__"
