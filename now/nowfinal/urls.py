from django.urls import path
# from django.contrib.auth import views as auth_views

from .views import nowfinal
urlpatterns = [
    path('', nowfinal, name='nowfinal'),
]