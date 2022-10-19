from rest_framework_gis.serializers import GeoFeatureModelSerializer


from . models import  StateDissolve
from . models import Districts
from . models import Tahesil



class StateDissolveSubSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = StateDissolve
		fields = '__all__'
		geo_field = 'geom'


class DistrictsSubSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Districts
		fields = '__all__'
		geo_field = 'geom'

class TahesilSubSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Tahesil
		fields = '__all__'
		geo_field = 'geom'