# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model) :
    category = models.CharField(max_length = 120)
    
    class Meta :
        verbose_name_plural = 'Categories'
    
    def __str__(self) :
        return self.category

    def __unicode__(self) :
        return self.category

class todo(models.Model) :
    title = models.CharField(max_length = 120)
    content = models.CharField(max_length = 120)
    due_date = models.DateField()
    category = models.ForeignKey(Category)

    class Meta :
        verbose_name_plural = 'todoes'

    def __str__(self) :
        return self.title

    def __unicode__(self):
        return self.title

