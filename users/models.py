from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nickname", default="")
    birday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(max_length=50, choices=(("male","male"), ("female", "female")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "userinfor"
        verbose_name_plural = verbose_name