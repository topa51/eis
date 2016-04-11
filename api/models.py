from django.db import models
from django.utils import timezone
from django_unixdatetimefield import UnixDateTimeField
import time
from datetime import datetime
import json

class Ship(models.Model):
	speed = models.DecimalField(max_digits=65, decimal_places=2)
	courseAngle = models.DecimalField(max_digits=65, decimal_places=2)
	lat = models.DecimalField(max_digits=65, decimal_places=10)
	lng = models.DecimalField(max_digits=65, decimal_places=10)
	name = models.CharField(max_length=200)
	
	timestamp = models.DateTimeField(
			default=timezone.now)
	unixTimestamp = models.IntegerField(default=int(time.mktime(timezone.now().timetuple())))

	def publish(self):
		self.timestamp = timezone.now()
		self.unixTimestamp = int(time.mktime(timezone.now().timetuple()))
		self.save()

	def __str__(self):
		return self.name

class Invite(models.Model):
	key = models.CharField(max_length=255)
	deeplink = models.CharField(max_length=255)
	ip = models.CharField(max_length=255)
	timestamp = models.DateTimeField(
			default=timezone.now)
	unixTimestamp = models.IntegerField(default=int(time.mktime(timezone.now().timetuple())))


	def publish(self):
		self.timestamp = timezone.now()
		self.save()

	def __str__(self):
		return self.key		

class Janusz(models.Model):
	
	januszType = models.IntegerField()
	lat = models.DecimalField(max_digits=65, decimal_places=10)
	lng = models.DecimalField(max_digits=65, decimal_places=10)
	count = models.IntegerField(default=1)
	
	timestamp = models.DateTimeField(
			default=timezone.now)
	unixTimestamp = models.IntegerField(default=int(time.mktime(timezone.now().timetuple())))

	def publish(self):
		self.timestamp = timezone.now()
		self.unixTimestamp = int(time.mktime(timezone.now().timetuple()))
		self.save()

class GeoSearch(models.Model):
	
	pageId = models.IntegerField();
	lat = models.DecimalField(max_digits=65, decimal_places=10)
	lng = models.DecimalField(max_digits=65, decimal_places=10)
	desc = models.TextField()
	imageurl = models.CharField(max_length=255)

	def __init__(self, pageId='', desc=''):
		self.pageId = pageId
		self.desc = desc

	def _asdict(self):
		return self.__dict__

	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)

class Image(models.Model):
	title = models.CharField(max_length=255)
						
	
	
		
