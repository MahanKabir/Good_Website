from django import forms

from blog.models import Blog
from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']