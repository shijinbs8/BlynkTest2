# Generated by Django 4.2.2 on 2023-06-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_bulb_classroom_delete_class_bulb_classroom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bulb",
            name="status",
            field=models.IntegerField(choices=[(0, "Off"), (1, "On")], default=0),
        ),
    ]
