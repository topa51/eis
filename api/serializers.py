from rest_framework import serializers
from .models import Ship

class ShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ship
        fields = ('speed', 'courseAngle', 'lat', 'lng', 'name', 'timestamp')