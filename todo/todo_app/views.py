# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request) :
    context_dict = {}
    if request.method == 'POST' :
        todo = request.POST.getlist('todo[]')
        print(todo)
        context_dict['todo'] = todo
        print(context_dict)
        return render(request,'todo/display.html',context_dict)
    return render(request,'todo/index.html')