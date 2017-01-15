from django.forms import ModelForm
from django import forms

from models import Tickets
from models import Sector
from django.db.models import Q


class TicketForm(ModelForm):

    def __init__(self, event_id, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['sector'].queryset = Sector.objects.filter(event=event_id)
        self.fields['event'].initial = event_id
        self.fields['event'].widget = forms.HiddenInput()

    class Meta:
        model = Tickets
        fields = ['event', 'guest_name', 'guest_surname', 'guest_email', 'column', 'row', 'sector']

    def clean(self):
        row = self.cleaned_data.get('row')
        column = self.cleaned_data.get('column')
        sector = self.cleaned_data.get('sector')

        is_free = False
        try:
            ticket = Tickets.objects.get(
                Q(row=self.cleaned_data['row'])
                & Q(column=self.cleaned_data['column'])
                & Q(event=self.cleaned_data['event'])
                & Q(sector=self.cleaned_data['sector'])
            )
        except Tickets.DoesNotExist:
            is_free = True

        if row < 0 | column < 0:
            raise forms.ValidationError('Invalid row or column')
        elif not is_free:
            raise forms.ValidationError('Ticket was booked by someone else')

