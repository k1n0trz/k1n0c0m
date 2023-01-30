from django.contrib import admin
from .models import Servicio, Solicitud

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

class SolicitudAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", )

# Register your models here.
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)