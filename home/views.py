""" home page view """
from django.shortcuts import render

# Create your views here.


def index(request):
    """ creates the home page view """
    return render(request, 'home/index.html')
