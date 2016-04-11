from rest_framework import serializers
from .models import Ship, Invite, Janusz, GeoSearch

class ShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ship
        fields = ('id','speed', 'courseAngle', 'lat', 'lng', 'name', 'timestamp', 'unixTimestamp')


class InviteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Invite;
		fields = ('id', 'key', 'deeplink', 'timestamp', 'unixTimestamp')

class JanuszSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Janusz;
		fields = ('id', 'januszType', 'lat', 'lng', 'count')		

class GeoSearchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GeoSearch;
		fields = ('pageId')		
						
