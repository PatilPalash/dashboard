from django.contrib.gis import admin


from . models import StateDissolve
from . models import Districts
from . models import Tahesil




admin.site.register(StateDissolve, admin.ModelAdmin)
admin.site.register(Districts, admin.ModelAdmin)
admin.site.register(Tahesil, admin.ModelAdmin)
