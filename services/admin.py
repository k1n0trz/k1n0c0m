from django.contrib import admin
from .models import Servicio, Solicitud, Numero

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

class SolicitudAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", )

class NumeroAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Numero, NumeroAdmin)