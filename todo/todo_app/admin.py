# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo_app.models import Category, todo

# Register your models here.
class todoAdmin(admin.ModelAdmin) :
    list_display = ('title','content','category','due_date',)

admin.site.register(Category)
admin.site.register(todo,todoAdmin)