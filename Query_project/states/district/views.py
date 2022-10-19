from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import viewsets

# Create your views here.
from . models import StateDissolve
from . models import Districts
from . models import Tahesil

from . serializers import  StateDissolveSubSerializer
from . serializers import  DistrictsSubSerializer
from . serializers import  TahesilSubSerializer




class NormalMap(TemplateView):
	template_name = 'index.html'


class StateDissolveViewSet(viewsets.ModelViewSet):
	serializer_class = StateDissolveSubSerializer
	queryset = StateDissolve.objects.all()
	


class DistrictsViewSet(viewsets.ModelViewSet):
	serializer_class = DistrictsSubSerializer
	queryset = Districts.objects.all()


class TahesilViewSet(viewsets.ModelViewSet):
	serializer_class = TahesilSubSerializer
	queryset = Tahesil.objects.all()


def showstate(request):
	template_name = 'index.html'
	# answer=StateDissolve.objects.all().values("state").distinct()
	# results=Districts.objects.all().values("dist").distinct()
	answer=StateDissolve.objects.all()
	results=Districts.objects.all()
	return render(request, template_name,{"StatesModel":answer, "DistrictsModel":results})



# .values('state','dist').distinct()