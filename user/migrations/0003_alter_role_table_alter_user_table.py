# Generated by Django 4.2 on 2023-04-13 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_user_role"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="role",
            table="role",
        ),
        migrations.AlterModelTable(
            name="user",
            table="user",
        ),
    ]
