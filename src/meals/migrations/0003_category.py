# Generated by Django 4.1.3 on 2022-11-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0002_alter_meals_options_meals_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
    ]