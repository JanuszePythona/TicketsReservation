from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from forms import TicketForm
from models import Event
from models import Sector


def index(request):
    template = loader.get_template('index.html')
    context = {
        'users': User.objects.all(),
        'events': Event.objects.all()
    }
    return HttpResponse(template.render(context, request))


def view_event(request, event_id):
    template = loader.get_template('event.html')
    context = {
        'event': Event.objects.get(id=event_id),
        'sectors': Sector.objects.filter(event=event_id)
    }
    return HttpResponse(template.render(context, request))


def place_reservation(request, event_id):
    if request.method == 'POST':
        form = TicketForm(event_id, request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            data = form.cleaned_data
            email = data['guest_email']
            send_mail('Test', 'test', 'janusze.pythona@gmail.com', [email])
            return render(request, 'success_res.html')
    else:
        form = TicketForm(event_id)
    return render(request, 'place_reservation.html', {'form': form})


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
        'events': Event.objects.filter(user_id=request.user.id)
    }
    return HttpResponse(template.render(context, request))
