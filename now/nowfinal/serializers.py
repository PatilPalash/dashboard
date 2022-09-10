#src/gis_rest_project/nairobi_hospitals_api/serializers.py
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import MhTotalDist

class MhTotalDistSubSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = MhTotalDist
		fields = '__all__'
		geo_field = 'geom'

    
# class NairobiHealthFacilitiesSerializer(GeoFeatureModelSerializer):
    	
# 	distance = serializers.CharField()

# 	class Meta:
# 		model = NairobiHealthFacilities
# 		fields = '__all__'
# 		geo_field = 'geom'
# 		read_only_fields = ['distance']