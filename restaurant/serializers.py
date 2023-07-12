from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, Menu
import datetime


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'number_of_guests', 'booking_date']


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']