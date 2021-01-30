from rest_framework import serializers
from .models import UserProfile
from allauth.account.adapter import get_adapter
from rest_auth.registration import serializers as RegisterSerializer
from roboPortal.models import portalUser


class UserProfileSerializer(serializers.ModelSerializer, RegisterSerializer.RegisterSerializer):

    password1 = serializers.CharField(write_only=True)
    extra_kwargs = {
        'password1' : {
            'write_only':True,
            'style':{'input_type':'password'}
        }
    }

    class Meta:
        model = UserProfile
        fields = ('email','name','phone_no','password','password1')
        extra_kwargs = {
            'password' : {
                'write_only':True,
                'style':{'input_type':'password'}
            },
            'password1' : {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(("The two password fields didn't match."))
        return data

    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email = validated_data.get('email'),
            name = validated_data.get('name'),
            phone_no = validated_data.get('phone_no'),
            password = validated_data.get('password')
        )
        a= portalUser(user = user)
        a.save()
        return user

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['name'] = self.validated_data.get('name')
        data_dict['phone_no'] = self.validated_data.get('phone_no')
        return data_dict

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ('id','email','name','phone_no')
        read_only_fields = ('email',)


class UserDetailsTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ('name',)
        read_only_fields = ('name',)
