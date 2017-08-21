# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import error
from .models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }

    return render(request, "courses/index.html", context)

def add_course(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        
        return redirect('/')
    
    course_name_input = request.POST.get('course_name')
    description_input = request.POST.get('description')
    print "course_name_input: {}; description_input: {}".format(course_name_input, description_input)
    
    
    desc_input = Description.objects.create(desc=description_input)
    Course.objects.create(name=course_name_input, description=desc_input)
    
    return redirect('/')
    
def destroy_course(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    print request.build_absolute_uri()
    return render(request, "courses/destroy_course.html", context)

def destroy_course_confirmed(request, course_id):
    print request.build_absolute_uri()
    course = Course.objects.get(id=course_id)
    course.delete()

    return redirect('/')