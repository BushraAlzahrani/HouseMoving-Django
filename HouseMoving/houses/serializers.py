from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'

class HouseSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = House
        exclude= ['owner',]

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class UserSerializerview(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class HousesSerializer(serializers.ModelSerializer):
    owner = UserSerializerview()
    class Meta:
        model = House
        fields = '__all__'

class AppointmentSerializerDriverPacker(serializers.ModelSerializer):
    house = HousesSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude= ['users',]



class BelongingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Belongings
        fields = '__all__'


class TrucksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovingTruck
        fields = '__all__'
