from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from .recievers import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                  validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
