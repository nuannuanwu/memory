# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from easy_thumbnails.fields import ThumbnailerImageField
from memory.models import Profile

def index(request, template_name="memory/memory_index.html"):
    profile = get_object_or_404(Profile, pk=1)
    thumb_url = profile.photo['normal'].url
    #width = profile.photo['normal'].image.size[0]
    height = profile.photo['normal']
    #print dir(height),'hhhhhhhhhhhhhhh'
    #print height.image,'hhhhhhhhhhh'
    print thumb_url,'uuuuuuuuuuuuuu'
    return render(request, template_name,{"thumb_url":thumb_url})

def test_index(request, template_name="memory/test_index.html"):
    space = range(30)
    return render(request, template_name,{"space":space})

def test_one(request, template_name="memory/test_one.html"):
    profile = get_object_or_404(Profile, pk=1)
    space = range(50)
    thumb_url = profile.photo['normal'].url
    return render(request, template_name,{"space":space,"thumb_url":thumb_url})
def test_two(request, template_name="memory/test_two.html"):
    space = range(30)
    return render(request, template_name,{"space":space})

def test_one_extra(request, template_name="memory/test_one_extra.html"):
    profile = get_object_or_404(Profile, pk=1)
    space = range(50)
    thumb_url = profile.photo['normal'].url
    return render(request, template_name,{"space":space,"thumb_url":thumb_url})
