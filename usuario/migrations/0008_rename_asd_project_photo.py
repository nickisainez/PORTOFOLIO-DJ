# Generated by Django 4.1.4 on 2022-12-11 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0007_rename_photo_project_asd"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="asd",
            new_name="photo",
        ),
    ]
