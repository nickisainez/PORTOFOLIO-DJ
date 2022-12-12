# Generated by Django 4.1.4 on 2022-12-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuario", "0002_delete_customers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("photo", models.ImageField(upload_to="miportofolio/images")),
                ("url", models.URLField()),
            ],
        ),
    ]
