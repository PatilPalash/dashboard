from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views
from .views import NormalMap, StateDissolveViewSet
from .views import NormalMap, DistrictsViewSet
from .views import NormalMap, TahesilViewSet
from .views import showstate
 





urlpatterns = [
    path('',views.showstate),
    # path('',views.showdistic),
    path('showstate/', showstate, name='showstate'),
    path('', NormalMap.as_view(), name='NormalMap'),
    path('StateDissolveViewSet/', StateDissolveViewSet.as_view({'get': 'list'}), name='StateDissolveViewSet'),
    path('DistrictsViewSet/', DistrictsViewSet.as_view({'get': 'list'}), name='DistrictsViewSet'),
    path('TahesilViewSet/', TahesilViewSet.as_view({'get': 'list'}), name='TahesilViewSet'),
]