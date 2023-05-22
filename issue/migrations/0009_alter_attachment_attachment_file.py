# Generated by Django 4.2 on 2023-05-12 10:22

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0008_rename_text_comment_comment_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="attachment_file",
            field=models.FileField(
                max_length=1000,
                storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                upload_to="documents/",
            ),
        ),
    ]