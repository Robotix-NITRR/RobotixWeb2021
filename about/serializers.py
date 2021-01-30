from rest_framework import serializers
from .models import Convenor,Coordinator,Manager,HeadCoordinator

class ConvenorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenor
        fields = '__all__'

class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class HeadCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCoordinator
        fields = '__all__'
