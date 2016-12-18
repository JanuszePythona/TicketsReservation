from django.http import HttpResponse
from django.template import loader

from .models import *


def login(request):
    template = loader.get_template('registration/login.html')

    return HttpResponse(template.render(request))


