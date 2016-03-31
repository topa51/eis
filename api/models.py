from django.db import models
from django.utils import timezone
from django_unixdatetimefield import UnixDateTimeField
import time
from datetime import datetime

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
	
	timestamp = models.DateTimeField(
			default=timezone.now)


	def publish(self):
		self.timestamp = timezone.now()
		
		self.save()

	def __str__(self):
		return self.key		

class Janusz(models.Model):
	
	januszType = models.IntegerField()
	lat = models.DecimalField(max_digits=65, decimal_places=10)
	lng = models.DecimalField(max_digits=65, decimal_places=10)
	count = models.IntegerField(default=0)
	
	timestamp = models.DateTimeField(
			default=timezone.now)
	unixTimestamp = models.IntegerField(default=int(time.mktime(timezone.now().timetuple())))

	def publish(self):
		self.timestamp = timezone.now()
		self.unixTimestamp = int(time.mktime(timezone.now().timetuple()))
		self.save()
