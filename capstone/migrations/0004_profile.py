# Generated by Django 3.1.7 on 2021-04-14 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_shouldieat_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('occupation', models.CharField(max_length=255)),
                ('interests', models.CharField(max_length=255)),
                ('about_me', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
