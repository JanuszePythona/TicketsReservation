from django.forms import ModelForm
from django import forms

from models import Event
from models import Sector


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'address', 'description', 'website', 'img_url']


class SectorForm(ModelForm):
    def __init__(self, event_id, *args, **kwargs):
        super(SectorForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['event'].initial = event_id
        self.fields['event'].widget = forms.HiddenInput()

    class Meta:
        model = Sector
        fields = ['name', 'max_column', 'max_row', 'price', 'event']
