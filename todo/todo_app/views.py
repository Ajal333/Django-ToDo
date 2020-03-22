# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from todo_app.models import Category, todo
from todo_app.forms import CategoryForm, todoForm

# Create your views here.

def index(request) :
    context_dict = {}
    if request.method == 'POST' :
        todo = request.POST.getlist('todo[]')
        sub_todo = request.POST.getlist('subtodo[]')
        print(todo)
        print(sub_todo)
        context_dict['todo'] = todo
        context_dict['subtodo'] = sub_todo
        print(context_dict)
        return render(request,'todo/display.html',context_dict)
    return render(request,'todo/index.html')

def add_category(request) :
    form = CategoryForm()
    if request.method == 'POST' :
        form = CategoryForm(request.POST)

        if form.is_valid() :
            form.save(commit=True)

            return HttpResponse('Category Added')
        
    return render(request,'todo/add_category.html',{'form':form})
        
def add_list(request) :
    form = todoForm() 
    if request.method == 'POST' :
        form = todoForm(request.POST)

        if form.is_valid() :
            form.save(commit=True)
            
            return HttpResponse('List Added')

    return render(request,'todo/add_list.html',{'form':form})
