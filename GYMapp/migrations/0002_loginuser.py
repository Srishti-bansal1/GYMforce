# Generated by Django 4.2.9 on 2024-02-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GYMapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loginuser",
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
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
    ]