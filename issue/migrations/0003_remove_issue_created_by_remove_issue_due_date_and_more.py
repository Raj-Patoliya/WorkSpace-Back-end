# Generated by Django 4.2 on 2023-05-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0002_issue_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="issue",
            name="due_date",
        ),
        migrations.RemoveField(
            model_name="issue",
            name="issue_key",
        ),
    ]
