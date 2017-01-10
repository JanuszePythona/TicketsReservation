from django.forms import ModelForm
from django import forms

from models import Tickets
from models import Sector


class TicketForm(ModelForm):
    def __init__(self, event_id, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['sector'].queryset = Sector.objects.filter(event = event_id)
        self.fields['event'].initial = event_id
        self.fields['event'].widget = forms.HiddenInput()

    class Meta:
        model = Tickets
        fields = ['event', 'guest_name', 'guest_surname', 'guest_email', 'column', 'row', 'sector']
