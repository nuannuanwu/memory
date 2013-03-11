# -*- coding: utf-8 -*-
from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    photo = ThumbnailerImageField(upload_to='memory/media/photos', blank=True)