from django import forms
from .models import Item

# Note: the Meta class gives our form some information about itself, such as which fields to render, or how to display errors
class ItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ['name', 'done']
