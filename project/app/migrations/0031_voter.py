# Generated by Django 3.2.6 on 2021-08-15 10:53

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_user_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('voter_id', models.IntegerField()),
                ('prefix', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('st', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('zone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
