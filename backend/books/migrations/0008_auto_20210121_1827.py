# Generated by Django 3.1.5 on 2021-01-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210121_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]