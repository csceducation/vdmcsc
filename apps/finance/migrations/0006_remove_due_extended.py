# Generated by Django 5.1 on 2024-08-23 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0005_due_due_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="due",
            name="extended",
        ),
    ]
