from django.contrib import admin
from .models import Installation, InstallationStandart, InstallationType, InstallationImage
# Register your models here.

admin.site.register(Installation)
admin.site.register(InstallationStandart)
admin.site.register(InstallationType)
admin.site.register(InstallationImage)
