# Generated by Django 3.1.5 on 2021-01-21 16:30

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210105_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='images',
            field=models.ImageField(default=django.db.models.fields.NullBooleanField, upload_to='images/'),
        ),
    ]