# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from easy_thumbnails.fields import ThumbnailerImageField
from memory.models import Profile
from django.http import HttpResponse
try:
    import simplejson as json
except ImportError:
    import json

def index(request, template_name="memory/index.html"):
    ctx = {}
    space = range(100)
    profile = get_object_or_404(Profile, pk=1)
    thumb_url = profile.photo['normal'].url
    page_data = range(15)
    ctx['page_data'] = page_data
    ctx['space'] = space
    ctx['thumb_url'] = thumb_url
    if request.is_ajax():
        page = int(request.GET.get("page",'1'))
        start = (page - 1) * 15
        end = page * 15
        page_data = range(15)
        ctx['page_data'] = page_data
        ctx['thumb_url'] = thumb_url
        template_name = "memory/test_one_container.html"
        return render(request, template_name, ctx)
    print ctx['page_data'],'ddddd'
    return render(request, template_name,ctx)
    

def index_test(request, template_name="memory/memory_index.html"):
    ctx = {}
    space = range(90)
    profile = get_object_or_404(Profile, pk=1)
    thumb_url = profile.photo['normal'].url
    page_data = range(15)
    ctx['page_data'] = page_data
    ctx['thumb_url'] = thumb_url
    ctx['space'] = space
    if request.is_ajax():
        page = int(request.GET.get("page",'0'))
        print page,'ppppppppppp'
        space = range(90)
        category_list = []
#        for s in space:
#            category_list.append({'thumb_url':thumb_url,"title":s})
        if page>3:
            category_list = []
            return HttpResponse('')
        template_name = "memory/memory_container.html"
        return render(request, template_name, ctx)
        return HttpResponse(json.dumps(category_list))
    return render(request, template_name,ctx)

def test_index(request, template_name="memory/test_index.html"):
    space = range(30)
    return render(request, template_name,{"space":space})

def test_one(request, template_name="memory/test_one.html"):
    ctx = {}
    page_data = range(16)
    ctx['page_data'] = page_data
    ctx['space'] = space
    if request.is_ajax():
        page = int(request.GET.get("page",'1'))
        start = (page - 1) * 16
        end = page * 16
        page_data = range(16)
        ctx['page_data'] = page_data
        template_name = "memory/test_one_container.html"
        return render(request, template_name, ctx)
    return render(request, template_name,ctx)
def test_two(request, template_name="memory/test_two.html"):
    from memory.templatetags import memory_tags
    space = range(90)
   
    return render(request, template_name,{"space":space})

def test_one_extra(request, template_name="memory/test_one_extra.html"):
    profile = get_object_or_404(Profile, pk=1)
    space = range(50)
    thumb_url = profile.photo['normal'].url
    return render(request, template_name,{"space":space,"thumb_url":thumb_url})

def test3(request, template_name="memory/test3.html"):
    space = range(90)
   
    return render(request, template_name,{"space":space})
