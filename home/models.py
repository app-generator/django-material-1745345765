# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    prename = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Geocache(models.Model):

    #__Geocache_FIELDS__
    gc_number = models.TextField(max_length=255, null=True, blank=True)
    gc_name = models.TextField(max_length=255, null=True, blank=True)
    gc_hint = models.TextField(max_length=255, null=True, blank=True)
    gc_notes = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Geocache_FIELDS__END

    class Meta:
        verbose_name        = _("Geocache")
        verbose_name_plural = _("Geocache")


class Gc_Logs(models.Model):

    #__Gc_Logs_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    gc_id = models.IntegerField(null=True, blank=True)
    gc_logtype = models.IntegerField(null=True, blank=True)

    #__Gc_Logs_FIELDS__END

    class Meta:
        verbose_name        = _("Gc_Logs")
        verbose_name_plural = _("Gc_Logs")



#__MODELS__END
