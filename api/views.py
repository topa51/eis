from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Ship, Invite, Janusz, GeoSearch, Image
from api.serializers import ShipSerializer, InviteSerializer, JanuszSerializer, GeoSearchSerializer
from api.filters import InviteFilter
from django.http import Http404
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view

# from pprint import pprint
# import django_filters
# import json
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
# from django.utils.datastructures import MultiValueDictKeyError
# from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urllib
import requests, re
import time
import json
import pprint

def render_invite(request):
	deeplink = request.GET.get('deeplink', '')
	return render(request, 'invite/invite.html', {'deeplink':deeplink})

def save_invite(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	ip = ""
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	key = request.POST.get('key', '')
	deeplink = request.POST.get('deeplink', '')
	timestamp = request.POST.get('timestamp', '')
	
	invite = Invite.objects.filter(key=key)
	if not invite.exists():
		invite = Invite()
	else :
		invite = invite[:1].get()
	invite.key = key
	invite.deeplink = deeplink
	invite.ip = ip;
	invite.timestamp = timestamp
	invite.publish()

	return HttpResponseRedirect("https://itunes.apple.com/pl/app/eniro-pa-sjon-free-nautical/id444222894?mt=8")

def default(o):
    return o._asdict()

@api_view(['GET'])
def get_wiki(request):
	lat = request.GET.get('lat', '')
	lon = request.GET.get('lon', '')

	locu_url = 'https://sv.wikipedia.org/w/api.php?action=query&prop=images&list=geosearch&gsradius=100&gscoord='+lat+'%7C'+lon+'&format=json'
	print(locu_url)
	
	resp = requests.get(locu_url)
	x = resp.json()
	geosearch = x["query"]["geosearch"]

	newgeosearch = []
	for geo in geosearch:
		newGeo = GeoSearch()
		newGeo.pageId = geo["pageid"]
		newGeo.lat = geo["lat"]
		newGeo.lon = geo["lon"]

		imageUrl = 'https://sv.wikipedia.org/w/api.php?action=query&prop=extracts|images&exintro=&explaintext=&format=json&pageids='+str(geo["pageid"])
		respImage = requests.get(imageUrl)
		respoImageJson = respImage.json()
		newGeo.desc = respoImageJson["query"]["pages"][str(newGeo.pageId)]["extract"]

		images = respoImageJson["query"]["pages"][str(newGeo.pageId)]["images"]
		
		if len(images) > 0:
			newImage = Image()
			newImage.title = images[0]["title"]
			
			words = newImage.title.split(":")
			if len(words):
				filename = words[1]
				fileUrl = "https://en.wikipedia.org/w/api.php?action=query&titles=File:"+filename+"&prop=imageinfo&iiprop=url&format=json"
				fileResp = requests.get(fileUrl)
				fileJson = fileResp.json()
				# print(fileUrl)
				try:
					imageInfo = fileJson["query"]["pages"]["33285577"]["imageinfo"][0]["url"]
					# imageInfo = fileJson["query"]["pages"]["-1"]["imageinfo"]["url"]
					print("###################")
					print(fileJson)
					print("*******************")
					print(imageInfo)
					print("###################")
					print("\n")
				except:
					try:
						imageInfo = fileJson["query"]["pages"]["-1"]["imageinfo"][0]["url"]
					except:
						imageInfo = ""
					
					# print(fileUrl)
					# print(fileJson)
					# fileJson["query"]["pages"]["-1"]["imageinfo"]["url"]
				
				newGeo.imageurl = imageInfo

			


		

		newgeosearch.append(json.JSONDecoder().decode(json.dumps(newGeo, default=default)))

	return Response(newgeosearch, status=status.HTTP_200_OK)

	

@api_view(['GET'])
def get_invite_by_key(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	ip = ""
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	
	key = request.GET.get('key', '')
	
	queryset = Invite.objects.filter(key=key)

	if not queryset.exists():
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		invite = queryset[:1].get()
		if invite.ip == ip:
			serializer = InviteSerializer(invite)
			return Response(serializer.data)
		else :
			return Response(status=status.HTTP_400_BAD_REQUEST)
	

class ShipList(generics.ListCreateAPIView):
	queryset = Ship.objects.all()
	serializer_class = ShipSerializer

class ShipDetail(APIView):
	def get_object(self, pk):
		try:
			return Ship.objects.get(pk=pk)
		except Ship.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		ship = self.get_object(pk)
		serializer = ShipSerializer(ship)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		ship = self.get_object(pk)
		serializer = ShipSerializer(ship, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		ship = self.get_object(pk)
		ship.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)   

class InviteList(generics.ListCreateAPIView):
	queryset = Invite.objects.all()
	serializer_class = InviteSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = InviteFilter

class InviteDetail(APIView):
	def get_object(self, pk):
		try:
			return Invite.objects.get(pk=pk)
		except Invite.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		invite = self.get_object(pk)
		serializer = InviteSerializer(invite)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		invite = self.get_object(pk)
		serializer = InviteSerializer(invite, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		invite = self.get_object(pk)
		invite.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)      

class JanuszList(generics.ListCreateAPIView):
	queryset = Janusz.objects.all()
	serializer_class = JanuszSerializer

class JanuszDetail(APIView):
	def get_object(self, pk):
		try:
			return Janusz.objects.get(pk=pk)
		except Janusz.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		janusz = self.get_object(pk)
		serializer = JanuszSerializer(janusz)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		janusz = self.get_object(pk)
		serializer = JanuszSerializer(janusz, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		janusz = self.get_object(pk)
		janusz.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)    


		
				  