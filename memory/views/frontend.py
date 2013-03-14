# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from easy_thumbnails.fields import ThumbnailerImageField
from memory.models import Profile

def index(request, template_name="memory/memory_index.html"):
    #profile = get_object_or_404(Profile, pk=1)
    #thumb_url = profile.photo['avatar'].url
    #print thumb_url,'uuuuuuuuuuuuuu'
    return render(request, template_name)

def test_index(request, template_name="memory/test_index.html"):
    space = range(30)
    return render(request, template_name,{"space":space})