from django.urls import path
# from django.contrib.auth import views as auth_views

from .views import NormalMap, StatesViewSet
from .views import NormalMap, DistrictsViewSet
from .views import NormalMap, TahesilViewSet






urlpatterns = [
    path('', NormalMap.as_view(), name='NormalMap'),
    path('StatesViewSet/', StatesViewSet.as_view({'get': 'list'}), name='StatesViewSet'),
    path('DistrictsViewSet/', DistrictsViewSet.as_view({'get': 'list'}), name='DistrictsViewSet'),
    path('TahesilViewSet/', TahesilViewSet.as_view({'get': 'list'}), name='TahesilViewSet'),
    

]