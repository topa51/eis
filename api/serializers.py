from rest_framework import serializers
from .models import Ship, Invite

class ShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ship
        fields = ('id','speed', 'courseAngle', 'lat', 'lng', 'name', 'timestamp', 'unixTimestamp')


class InviteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Invite;
		fields = ('id', 'key', 'deeplink', 'unixTimestamp')
