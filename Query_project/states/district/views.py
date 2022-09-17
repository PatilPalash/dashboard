from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

# Create your views here.
from . models import States
from . models import Districts
from . models import Tahesil

from . serializers import  StatesSubSerializer
from . serializers import  DistrictsSubSerializer
from . serializers import  TahesilSubSerializer




class NormalMap(TemplateView):
	template_name = 'index.html'


class StatesViewSet(viewsets.ModelViewSet):
	serializer_class = StatesSubSerializer
	queryset = States.objects.all()


class DistrictsViewSet(viewsets.ModelViewSet):
	serializer_class = DistrictsSubSerializer
	queryset = Districts.objects.all()


class TahesilViewSet(viewsets.ModelViewSet):
	serializer_class = TahesilSubSerializer
	queryset = Tahesil.objects.all()
