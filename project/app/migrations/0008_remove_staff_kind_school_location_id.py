# Generated by Django 4.0.3 on 2022-05-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_school_capacity_school_enrollment_alter_school_zone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='kind',
        ),
        migrations.AddField(
            model_name='school',
            name='location_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]