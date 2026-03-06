from rest_framework import serializers
from .models import Room, Roomcategory

class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Roomcategory
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'