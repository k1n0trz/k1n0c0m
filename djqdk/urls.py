"""djqdk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('politica-privacidad/', views.privacidad, name='privacidad'),
    path('politica-cookies/', views.cookies, name='cookies'),
    path('registro/', views.signup, name="registro"),
    path('solicitud/', views.solicitud, name="solicitud"),
    path('contacto/', views.contacto, name="contacto"),
    path('servicios/', views.servicios, name="servicios"),
    path('servicios/diseño-grafico/', views.diseno, name="diseno"),
    path('servicios/desarrollo-web-apps/', views.desarrollo, name="desarrollo"),
    path('servicios/cubrimiento-eventos/', views.eventos, name="eventos"),
    path('servicios/produccion-video-fotografia/', views.produccion, name="produccion"),
    path('servicios/marketing/', views.marketing, name="marketing"),
    path('servicios/blockchain/', views.blockchain, name="blockchain"),
    path('mis-servicios/servicios-completados/', views.servicios_completados, name="servicios_completados"),
    path('mis-servicios/', views.misservicios, name="mis-servicios"),
    path('mis-servicios/servicio/<int:servicio_id>', views.servicio_detalle, name="servicio_detalle"),
    path('mis-servicios/servicio/<int:servicio_id>/completa', views.complete_servicio, name="complete_servicio"),
    path('mis-servicios/servicio/<int:servicio_id>/eliminar', views.eliminar_servicio, name="eliminar_servicio"),
    path('mis-servicios/solicitar/', views.solicitar, name="solicitar"),
    path('logout/', views.signout, name="logout"),
    path('signin/', views.signin, name="signin"),
]
