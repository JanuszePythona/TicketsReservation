from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from forms import EventForm
from forms import SectorForm

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            return render(request, 'user_home.html')
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
            return render(request, 'user_home.html')
    else:
        form = SectorForm(event_id)
    return render(request, 'place_reservation.html', {'form': form})
