# Generated by Django 4.2.2 on 2023-06-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0004_alter_productpicture_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(default='static/shop_images/image1.png', upload_to='static/shop_images/'),
        ),
    ]
