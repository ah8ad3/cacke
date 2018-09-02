from django.shortcuts import render

from .messages import SIMPLE


def welcome(request):

    return render(request, 'index.html', {'message': SIMPLE.get('welcome')})
