# Generated by Django 4.2 on 2023-04-13 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0005_alter_project_created_by_alter_project_table_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IssueType",
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
                ("name", models.CharField(max_length=50)),
                (
                    "icon",
                    models.ImageField(blank=True, max_length=1000, upload_to="icons/"),
                ),
            ],
            options={
                "db_table": "issue_type",
            },
        ),
        migrations.CreateModel(
            name="Priority",
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
                ("name", models.CharField(max_length=50)),
                (
                    "icon",
                    models.ImageField(blank=True, max_length=1000, upload_to="icons/"),
                ),
            ],
            options={
                "db_table": "priority",
            },
        ),
        migrations.CreateModel(
            name="Status",
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
                ("name", models.CharField(max_length=50)),
                (
                    "icon",
                    models.ImageField(blank=True, max_length=1000, upload_to="icons/"),
                ),
            ],
            options={
                "db_table": "status",
            },
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("issue_summary", models.CharField(max_length=200)),
                ("issue_key", models.CharField(max_length=20)),
                ("issue_description", models.TextField()),
                ("due_date", models.DateField()),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_date", models.DateTimeField()),
                (
                    "assignee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_type",
                        to="issue.issuetype",
                    ),
                ),
                (
                    "priority",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="priority",
                        to="issue.priority",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="project.project",
                    ),
                ),
                (
                    "reporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reporter",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="status",
                        to="issue.status",
                    ),
                ),
            ],
            options={
                "db_table": "issue",
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("text", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "issue_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to="issue.issue",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commentator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "comment",
            },
        ),
        migrations.CreateModel(
            name="Attachment",
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
                    "attachment_file",
                    models.ImageField(
                        blank=True, max_length=1000, upload_to="attachment/"
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "issue_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachment",
                        to="issue.issue",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="uploadedBy",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActivityLog",
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
                ("activityType", models.TextField()),
                ("prev", models.TextField()),
                ("latest", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "issue_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activityLog",
                        to="issue.issue",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "activityLog",
            },
        ),
    ]
