# Generated by Django 3.1.5 on 2021-06-10 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('nickname', models.CharField(blank=True, max_length=45, null=True)),
                ('sex', models.CharField(blank=True, max_length=45, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]