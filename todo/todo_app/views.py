# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from todo_app.models import Category, todo
from todo_app.forms import CategoryForm, todoForm

# Create your views here.

#def index(request) :
#    context_dict = {}
#    if request.method == 'POST' :
#        todo = request.POST.getlist('todo[]')
#        sub_todo = request.POST.getlist('subtodo[]')
#        print(todo)
#        print(sub_todo)
#        context_dict['todo'] = todo
#        context_dict['subtodo'] = sub_todo
#        print(context_dict)
#        return render(request,'todo/display.html',context_dict)
#    return render(request,'todo/index.html')

def add_category(request) :
    form1 = CategoryForm()
    if request.method == 'POST' :
        form = CategoryForm(request.POST)

        if form.is_valid() :
            form.save(commit=True)

            return render(request,'todo/add_category.html',{'message':'Category Added','form':form1})
        
    return render(request,'todo/add_category.html',{'form':form1})
        
def add_list(request) :
    category = Category.objects.all()
    todo_1 = todo.objects.all()
    form1 = todoForm() 
    if request.method == 'POST' :
        form = todoForm(request.POST)

        if form.is_valid() :
            form.save(commit=True)
            
            return render(request,'todo/add_list.html',{'message':'List Added','form':form1,'category':category,'todo':todo_1,})
        else :
            print('error')

    return render(request,'todo/add_list.html',{'form':form1,'category':category,'todo':todo_1,})

def view(request) :
    context_dict = {}
    category = Category.objects.all()
    main_list = todo.objects.all()

    if request.method == 'POST' :
        list1 = request.POST.getlist('todo[]')
        list2 = request.POST.getlist('cat[]')
        print(list1)
        print(list2)
        context_dict['todo'] = list1
        context_dict['category'] = list2
        context_dict['main_todo'] = main_list
        print(context_dict)
        return render(request,'todo/display.html',context_dict)

    context_dict['category'] = category
    context_dict['todo'] = main_list
    return render(request,'todo/view.html',context_dict)

def del_list(request, list1) :
    if request.method == 'POST' :
        form1 = todoForm()
        category = Category.objects.all()
        todo_1 = todo.objects.all()
        for data in todo_1 :
            if list1 == data.title :
                todo.objects.filter(title = list1).delete()
                print('{} is deleted'.format(list1))
            else :
                continue
        return render(request,'todo/add_list.html',{'form':form1,'category':category,'todo':todo_1})
    return render(request,'todo/add_list.html',{'form':form1,'category':category,'todo':todo_1})
    