from django.shortcuts import render
from .models import Category, Product


def category_list(request):
    categorys = Category.objects.all()
    return render(request, "index.html", context={"category": categorys})

