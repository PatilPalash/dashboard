# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class MhTotalDist(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    indiadpoly = models.FloatField(blank=True, null=True)
    indiadpo_1 = models.FloatField(blank=True, null=True)
    dist = models.CharField(max_length=254, blank=True, null=True)
    cnt_dist = models.FloatField(blank=True, null=True)
    sum_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.IntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_1 = models.IntegerField(blank=True, null=True)
    area_12 = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_total_dist'
