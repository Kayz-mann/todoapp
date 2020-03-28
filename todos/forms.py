from django import forms
from todos.models import Todo
from django.forms import ModelForm

class TodoForm(ModelForm):
  description = forms.CharField(max_length=255, required=True)
  
  class Meta:
    model = Todo
    fields = ( 'description',)