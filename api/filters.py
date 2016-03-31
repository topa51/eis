import django_filters
from .models import Invite
from .serializers import InviteSerializer
from rest_framework import filters
from rest_framework import generics

class InviteFilter(filters.FilterSet):
    
    class Meta:
        model = Invite
        fields = ['key', 'deeplink']