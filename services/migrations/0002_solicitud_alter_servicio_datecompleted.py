# Generated by Django 4.1.5 on 2023-01-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
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
                ("Nombre", models.CharField(max_length=200)),
                ("Email", models.EmailField(max_length=254)),
                ("Teléfono", models.CharField(max_length=200)),
                ("Ciudad", models.CharField(max_length=200)),
                ("Dirección", models.CharField(max_length=200)),
                (
                    "Servicio",
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
                ("Descripción", models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name="servicio",
            name="datecompleted",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]