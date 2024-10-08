# Generated by Django 5.1 on 2024-08-23 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enquiry", "0012_alter_enquiry_counsellor"),
        ("staffs", "0004_alter_staff_pincode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enquiry",
            name="counsellor",
            field=models.ForeignKey(
                default=None,
                limit_choices_to={"current_status": "active"},
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="staffs.staff",
            ),
        ),
    ]
