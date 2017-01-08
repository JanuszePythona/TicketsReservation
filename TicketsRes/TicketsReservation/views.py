from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

from models import Event


def index(request):
    template = loader.get_template('index.html')
    context = {
        'users': User.objects.all(),
        'activities': Event.objects.all()
    }
    return HttpResponse(template.render(context, request))


def view_event(request, event_id):
    template = loader.get_template('event.html')
    context = {
        'activity': Event.objects.get(id=event_id)
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contact.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

@login_required
def user_home(request):
    template = loader.get_template('user_home.html')
    context = {
        'activities': Event.objects.filter(user_id=request.user.id)
    }
    return HttpResponse(template.render(context, request))
