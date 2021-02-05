from rest_framework import serializers
from .models import DIY,FYI,sponsors


class DIYSerializer(serializers.ModelSerializer):

    class Meta:
        model = DIY
        fields = "__all__"


class FYISerializer(serializers.ModelSerializer):

    class Meta:
        model = FYI
        fields = "__all__"

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sponsors
        fields = '__all__'
