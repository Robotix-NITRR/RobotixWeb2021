from rest_framework import serializers
from .models import portalUser,Team
from allauth.account.adapter import get_adapter
from rest_auth.registration import serializers as RegisterSerializer
from roboPortal.models import portalUser,Team,problem_statement
from users.serializers import UserProfileSerializer,UserDetailsTeamSerializer

class portalUserSerializer(serializers.ModelSerializer):

    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = portalUser
        fields = ('user','resume','description','joined_team')

class teamserializer(serializers.ModelSerializer):

    admin = UserDetailsTeamSerializer(read_only=True)
    member = UserDetailsTeamSerializer(read_only=True,many=True)

    class Meta:
        model = Team
        fields = ('name','admin','member')

class RobothonSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem_statement
        fields = '__all__'
