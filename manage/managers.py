# -*- coding: utf-8 -*-
# from kinger.models import Group
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
import random
import datetime
from memory import settings
import os
from django.db import transaction


class SoftDeleteManager(models.Manager):
    '''
    | 给所有的查询过滤 ``is_delete`` 字段.
    '''
    use_for_related_fields = True
    def get_query_set(self):
        ''' 重写默认 ``Manager`` 获取 ``QuerySet`` 的对象，过滤已标记为删除的记录 '''
        return super(SoftDeleteManager, self).get_query_set().filter(is_delete=False)

    def all_with_deleted(self):
        ''' 满足需要获得已标记为删除的记录的需求 '''
        return super(SoftDeleteManager, self).get_query_set()

    def deleted_set(self):
        ''' 获得已标记为删除的记录 '''
        return super(SoftDeleteManager, self).get_query_set().filter(is_delete=True)

    #def get(self, *args, **kwargs):
    #    ''' if a specific record was requested, return it even if it's deleted '''
    #    return self.all_with_deleted().get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        ''' if pk was specified as a kwarg, return even if it's deleted '''
        if 'is_delete' in kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_query_set().filter(*args, **kwargs)














