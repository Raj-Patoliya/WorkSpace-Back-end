# Generated by Django 4.2 on 2023-05-12 10:23

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0009_alter_attachment_attachment_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="attachment_file",
            field=models.FileField(
                max_length=1000,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="documents/",
            ),
        ),
    ]
