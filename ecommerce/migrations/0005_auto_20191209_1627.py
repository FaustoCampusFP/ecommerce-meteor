# Generated by Django 2.2.6 on 2019-12-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20191209_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='shoes/no-disponible.png', upload_to='shoes'),
        ),
    ]
