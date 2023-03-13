from rest_framework import serializers
from rep_app.models import Company, User, Device


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('com_name', 'com_id', 'dev_status', 'user_id_f')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_id', 'device_id_f')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_name', 'device_id')

