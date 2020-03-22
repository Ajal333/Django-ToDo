from django import forms
from todo_app.models import Category, todo
from datetime import datetime

class CategoryForm(forms.ModelForm) :
    category = forms.CharField(max_length = 120, help_text="Enter Your Category: ")

    class Meta:
        model = Category
        fields = ('category',)

class todoForm(forms.ModelForm) :
    title = forms.CharField(max_length = 120, help_text="Your title: ")
    content = forms.CharField(max_length = 120, help_text= "Your description: ")
    category = forms.ModelChoiceField(queryset = Category.objects.all(),empty_label="Select One",help_text='Select Category')
    class Meta:
        model = todo
        exclude = ('date_created','due_date',)