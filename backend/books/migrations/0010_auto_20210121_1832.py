# Generated by Django 3.1.5 on 2021-01-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210121_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
