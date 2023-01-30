# Generated by Django 4.1.5 on 2023-01-30 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Solicitud",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("correo", models.EmailField(max_length=200)),
                ("telefono", models.CharField(max_length=200)),
                ("ciudad", models.CharField(max_length=200)),
                ("direccion", models.CharField(max_length=200)),
                (
                    "contrato",
                    models.IntegerField(
                        choices=[
                            (1, "Seleccione un servicio"),
                            (2, "Marketing"),
                            (3, "Diseño Gráfico"),
                            (4, "Desarrollo Web"),
                            (5, "Producción Fotográfica/Audiovisual"),
                            (6, "Tecnología Blockchain"),
                            (7, "Otros..."),
                        ],
                        default=1,
                    ),
                ),
                ("descripcion", models.TextField(blank=True)),
                ("creado", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("datecompleted", models.DateTimeField(blank=True, null=True)),
                ("important", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
