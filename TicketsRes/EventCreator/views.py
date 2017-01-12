from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from TicketsReservation.views import view_event
from forms import EventForm
from forms import SectorForm
from django.template import loader
from django.http import HttpResponse
from models import Event
from TicketsReservation.models import Tickets
from django.core.mail import EmailMessage

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            return view_event(request, event.id)
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


@login_required()
def add_sector(request, event_id):
    if request.method == 'POST':
        form = SectorForm(event_id, request.POST)
        if form.is_valid():
            sector = form.save(commit=False)
            sector.user = request.user
            sector.save()

            return view_event(request, event_id)
    else:
        form = SectorForm(event_id)
    return render(request, 'add_sector.html', {'form': form})


def confirm_cancel(request, event_id):
    template = loader.get_template('confirm_cancelation.html')
    context = {
        'event': Event.objects.get(id=event_id)
    }
    return HttpResponse(template.render(context, request))


def cancel_event(request, event_id):
    event = Event.objects.get(id=event_id)

    tickets = Tickets.objects.filter(event_id = event_id)

    for ticket in tickets:
        content = 'We are sorry to inform that the event: ' + str(ticket.event.name) + ' was canceled.'
        mail = EmailMessage('Event canceled', content, 'janusze.pythona@gmail.com', [ticket.guest_email])
        mail.send()

    event.delete()
    return render(request, 'user_home.html')


def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return view_event(request, event_id)
    return render(request, 'edit_event.html', {'form': form})

