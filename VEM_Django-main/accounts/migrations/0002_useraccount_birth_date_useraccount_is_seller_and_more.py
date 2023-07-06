# Generated by Django 4.2.2 on 2023-06-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='location',
            field=models.CharField(default='Location', max_length=100),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profile_pictures/profile.png', null=True, upload_to='static/profile_pictures/'),
        ),
    ]