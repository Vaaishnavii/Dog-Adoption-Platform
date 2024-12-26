# Generated by Django 5.1.2 on 2024-12-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizResponse",
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
                ("time_dedication", models.CharField(max_length=50)),
                ("living_space", models.CharField(max_length=50)),
                ("grooming", models.CharField(max_length=10)),
                ("children", models.CharField(max_length=50)),
                ("activity_level", models.CharField(max_length=50)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
