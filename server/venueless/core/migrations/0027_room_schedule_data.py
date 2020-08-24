# Generated by Django 3.0.8 on 2020-08-08 14:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_exhibitorlink_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="schedule_data",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
