from django.forms import ModelForm
from .models import Servicio, Solicitud

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['title', 'description', 'important']

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = ['nombre', 'correo', 'telefono', 'ciudad', 'direccion', 'contrato', 'descripcion']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({
                'class': 'form-control',
            })