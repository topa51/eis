from django.db import models
from django.utils import timezone

class Ship(models.Model):
	speed = models.DecimalField(max_digits=65, decimal_places=2)
	courseAngle = models.DecimalField(max_digits=65, decimal_places=2)
	lat = models.DecimalField(max_digits=65, decimal_places=2)
	lng = models.DecimalField(max_digits=65, decimal_places=2)
	name = models.CharField(max_length=200)
	
	timestamp = models.DateTimeField(
			default=timezone.now)

	def publish(self):
		self.timestamp = timezone.now()
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