from django import forms

from .models import Event

MAX_EVENT_NAME_LENGTH = 60
MAX_EVENT_DESC_LENGTH = 240
MAX_EVENT_TEXT_LENGTH = 840

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'text']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > MAX_EVENT_NAME_LENGTH:
            raise forms.ValidationError("This event name is too long")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) > MAX_EVENT_DESC_LENGTH:
            raise forms.ValidationError("This event description is too long")
        return description

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if len(text) > MAX_EVENT_TEXT_LENGTH:
            raise forms.ValidationError("This event text is too long")
        return text