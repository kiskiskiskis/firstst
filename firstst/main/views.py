from django.shortcuts import render
from django.views import View

def base(request):
    return render(request, 'base.html')