from django import forms
from .models import Item


class ItemForm(forms.modelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']