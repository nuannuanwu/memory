# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models

from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.admin import widgets, helpers
from django.contrib.admin.util import unquote

from memory import settings
from django.core.urlresolvers import reverse
from memory.models import Profile


admin.site.register(Profile)




