from rest_framework_gis.serializers import GeoFeatureModelSerializer


from . models import  States
from . models import Districts
from . models import Tahesil



class StatesSubSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = States
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