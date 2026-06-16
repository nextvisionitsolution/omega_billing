from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['category', 'name']

        widgets = {

            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }