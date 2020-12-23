# Generated by Django 3.0.11 on 2020-12-22 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0036_janusserver"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatEventReaction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reaction", models.TextField()),
                (
                    "chat_event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reactions",
                        to="core.ChatEvent",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_reactions",
                        to="core.User",
                    ),
                ),
            ],
        ),
    ]
