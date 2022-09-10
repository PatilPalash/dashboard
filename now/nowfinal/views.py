from django.shortcuts import render, HttpResponse

#src/gis_rest_project/nairobi_hospitals_api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action

from . models import  MhTotalDist
from . serializers import  MhTotalDistSubSerializer

class MhTotalDistViewSet(viewsets.ModelViewSet):
	serializer_class = MhTotalDistSubSerializer
	queryset = MhTotalDist.objects.all()


def home(request):
    return render(request, 'index.html')

