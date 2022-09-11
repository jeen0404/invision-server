from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from .models import PhoneToken, User
from django.core.validators import RegexValidator


class PhoneTokenCreateSerializer(ModelSerializer):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message='Phone no must be in the format of +99999999. 14 digit allowed')
    phone_number = serializers.CharField()

    class Meta:
        model = PhoneToken
        fields = ('phone_number',)


class PhoneTokenValidateSerializer(ModelSerializer):
    token_id = serializers.CharField(max_length=36)
    otp = serializers.CharField(max_length=40)

    class Meta:
        model = PhoneToken
        fields = ('token_id', 'otp')


class CheckUsernameAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class SearchViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'name', 'profile_image',)


class AddDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'profile_image')


class ProfileSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(allow_null=True, read_only=True)

    class Meta:
        model = User
        fields = ('user_id', 'phone_number', 'username', 'name', 'profile_image', 'organization')
