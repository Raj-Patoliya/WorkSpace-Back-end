# Generated by Django 4.2 on 2023-04-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_profileavtar"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserAvtar",
        ),
    ]
