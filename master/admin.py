from django.contrib import admin

from . import models


admin.site.register(models.Corporate)
admin.site.register(models.Team)
admin.site.register(models.Customer)
