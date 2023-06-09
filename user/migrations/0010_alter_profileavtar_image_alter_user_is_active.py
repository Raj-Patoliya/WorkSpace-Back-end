# Generated by Django 4.2.1 on 2023-05-23 04:14

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_alter_user_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileavtar",
            name="image",
            field=models.ImageField(
                blank=True,
                max_length=1000,
                storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                upload_to="avtar",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
