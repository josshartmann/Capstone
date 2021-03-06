# Generated by Django 3.1.7 on 2021-04-28 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0010_quotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about_me',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_place',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
