# Generated by Django 4.2 on 2023-04-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_remove_useravtar_icon_useravtar_avtar"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileAvtar",
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
                (
                    "image",
                    models.ImageField(blank=True, max_length=1000, upload_to="avtar"),
                ),
            ],
            options={
                "db_table": "user_profile",
            },
        ),
    ]
