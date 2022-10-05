from django.http import HttpResponse
from django.shortcuts import render

from .adapter import Model

library = Model()


def responseBase(request):
    return render(request, 'public/base.html')


def responseMap(request):
    return render(request, 'public/example.html')
