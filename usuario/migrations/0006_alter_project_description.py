# Generated by Django 4.1.4 on 2022-12-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0005_project_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(),
        ),
    ]