from django.db import models
from django.contrib.gis.db import models


# Create your models here.



# class States(models.Model):
#     gid = models.AutoField(primary_key=True)
#     layer = models.CharField(max_length=17, blank=True, null=True)
#     area = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     perimeter = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     indiasln_field = models.IntegerField(db_column='indiasln_', blank=True, null=True)  # Field renamed because it ended with '_'.
#     indiasln_i = models.IntegerField(blank=True, null=True)
#     state = models.CharField(max_length=20, blank=True, null=True)
#     shape_leng = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     shape_area = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     geom = models.MultiPolygonField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'states'

class StateDissolve(models.Model):
    gid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_dissolve'
    
    def __str__(self):
        return self.state

# class Districts(models.Model):
#     gid = models.AutoField(primary_key=True)
#     layer = models.CharField(max_length=17, blank=True, null=True)
#     area = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     perimeter = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     indiadpoly = models.IntegerField(blank=True, null=True)
#     indiadpo_1 = models.IntegerField(blank=True, null=True)
#     dist = models.CharField(max_length=254, blank=True, null=True)
#     cnt_dist = models.IntegerField(blank=True, null=True)
#     sum_area = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     state = models.CharField(max_length=50, blank=True, null=True)
#     type = models.CharField(max_length=50, blank=True, null=True)
#     symbol = models.SmallIntegerField(blank=True, null=True)
#     shape_leng = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     shape_area = models.DecimalField(max_digits=65535, decimal_places=45535, blank=True, null=True)
#     area_1 = models.SmallIntegerField(blank=True, null=True)
#     area_12 = models.CharField(max_length=50, blank=True, null=True)
#     geom = models.MultiPolygonField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'districts'

class Districts(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    indiadpoly = models.IntegerField(blank=True, null=True)
    indiadpo_1 = models.IntegerField(blank=True, null=True)
    dist = models.CharField(max_length=254, blank=True, null=True)
    cnt_dist = models.IntegerField(blank=True, null=True)
    sum_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.SmallIntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_1 = models.SmallIntegerField(blank=True, null=True)
    area_12 = models.CharField(max_length=50, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'

    def __str__(self):
        return self.dist
    
   


class Tahesil(models.Model):
    gid = models.AutoField(primary_key=True)
    id_0 = models.FloatField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    id_1 = models.FloatField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True, null=True)
    id_2 = models.FloatField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True, null=True)
    id_3 = models.FloatField(blank=True, null=True)
    name_3 = models.CharField(max_length=75, blank=True, null=True)
    ccn_3 = models.FloatField(blank=True, null=True)
    cca_3 = models.CharField(max_length=15, blank=True, null=True)
    type_3 = models.CharField(max_length=50, blank=True, null=True)
    engtype_3 = models.CharField(max_length=50, blank=True, null=True)
    nl_name_3 = models.CharField(max_length=75, blank=True, null=True)
    varname_3 = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tahesil'




    