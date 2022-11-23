# Generated by Django 4.1.3 on 2022-11-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meals",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=500)),
                ("people", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("preparation_time", models.IntegerField()),
                ("image", models.ImageField(upload_to="meals/")),
            ],
        ),
    ]
