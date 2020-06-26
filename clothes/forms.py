from django import forms
from .models import Category


class MultipleImageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
