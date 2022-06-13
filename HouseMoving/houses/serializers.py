from rest_framework import serializers
from .models import *


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
