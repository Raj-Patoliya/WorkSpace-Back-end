# Generated by Django 4.2 on 2023-05-04 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0004_attachment_updated_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attachment",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="attachment",
            name="user",
        ),
    ]
