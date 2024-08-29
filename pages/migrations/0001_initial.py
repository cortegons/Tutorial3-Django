# Generated by Django 5.1 on 2024-08-21 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
