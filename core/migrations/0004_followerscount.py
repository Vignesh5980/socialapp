# Generated by Django 5.0 on 2024-01-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_likepost"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
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
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]