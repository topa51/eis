from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Ship
from api.serializers import ShipSerializer
# from django.http import Http404
# from rest_framework import generics
# from pprint import pprint
# import django_filters
# import json
# from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
# from django.utils.datastructures import MultiValueDictKeyError
# from datetime import datetime

class ShipList(generics.ListCreateAPIView):
  queryset = Ship.objects.all()
    serializer_class = ShipSerializer