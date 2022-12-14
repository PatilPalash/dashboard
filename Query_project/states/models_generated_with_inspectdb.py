# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainappPokemoncenters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    master = models.CharField(max_length=50)
    rating = models.IntegerField()
    location = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mainapp_pokemoncenters'


class MhForest(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    srims_code = models.FloatField(blank=True, null=True)
    lu_code = models.CharField(max_length=12, blank=True, null=True)
    descriptio = models.CharField(max_length=70, blank=True, null=True)
    area_sq_km = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_forest'


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


class NagpurForReproject(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    forest_field = models.FloatField(db_column='forest_', blank=True, null=True)  # Field renamed because it ended with '_'.
    forest_id = models.FloatField(blank=True, null=True)
    srims_code = models.FloatField(blank=True, null=True)
    descriptio = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagpur_for_reproject'


class NagpurForReprojectWgs(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    forest_field = models.FloatField(db_column='forest_', blank=True, null=True)  # Field renamed because it ended with '_'.
    forest_id = models.FloatField(blank=True, null=True)
    srims_code = models.FloatField(blank=True, null=True)
    descriptio = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagpur_for_reproject_wgs'


class PointcloudFormats(models.Model):
    pcid = models.IntegerField(primary_key=True)
    srid = models.IntegerField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointcloud_formats'


class PracticeCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    layer = models.CharField(max_length=17)
    area = models.FloatField()
    perimeter = models.FloatField()
    indiadpoly = models.BigIntegerField()
    indiadpo_1 = models.BigIntegerField()
    dist = models.CharField(max_length=254)
    cnt_dist = models.BigIntegerField()
    sum_area = models.FloatField()
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    symbol = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    area_1 = models.IntegerField()
    area_12 = models.CharField(max_length=50)
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'practice_city'


class PracticeIncidences(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'practice_incidences'


class StateDissolve(models.Model):
    gid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_dissolve'


class StateNag(models.Model):
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
    symbol = models.FloatField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_1 = models.FloatField(blank=True, null=True)
    area_12 = models.CharField(max_length=50, blank=True, null=True)
    forest_field = models.FloatField(db_column='forest_', blank=True, null=True)  # Field renamed because it ended with '_'.
    forest_id = models.FloatField(blank=True, null=True)
    srims_code = models.FloatField(blank=True, null=True)
    descriptio = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_nag'


class States(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    indiasln_field = models.IntegerField(db_column='indiasln_', blank=True, null=True)  # Field renamed because it ended with '_'.
    indiasln_i = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


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


class TmWorldBorders03(models.Model):
    gid = models.AutoField(primary_key=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    un = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    pop2005 = models.FloatField(blank=True, null=True)
    region = models.SmallIntegerField(blank=True, null=True)
    subregion = models.SmallIntegerField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_world_borders-0.3'
