from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    template = loader.get_template('index.html')
    context = {
        'users': User.objects.all()
    }
    return HttpResponse(template.render(context, request))


def user(request):
    template = loader.get_template('user.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
