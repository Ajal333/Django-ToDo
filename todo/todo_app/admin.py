# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo_app.models import Category, todo

# Register your models here.

admin.site.register(Category)
admin.site.register(todo)