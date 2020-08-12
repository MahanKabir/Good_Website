from django.shortcuts import render

# Create your views here.
from category.forms import CategoryForm


def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'admin/category/create.html')
