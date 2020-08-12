from pprint import pprint

from django.shortcuts import render

# Create your views here.
from blog.forms import BlogForm
from category.models import Category


def create(request, id):
    category = Category.objects.get(id = id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category_id = category.id
            f.save()
    return render(request, 'admin/blog/create.html', {'category': category})
