from django import forms
from .models import EventPost

class EventPostForm(forms.ModelForm):
    class Meta:
        model=EventPost
        fields=['title','description','image','event_date','event_coordinator']