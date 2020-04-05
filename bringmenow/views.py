from django.shortcuts import render, redirect
from .models import Product


def index(request):
    context = {}
    context['category'] = 'Fruits'

    return render(request, 'bringmenow/index.html', context)
