from enum import auto

from django import forms
#from django.forms import widgets

from  .models import Newuser
from datetime import datetime
class Add(forms.ModelForm):
    class Meta:
        model=Newuser
        fields = ['event_name','image','location','date']

        widgets={'event_name':forms.TextInput(attrs={'class':'form-control',}),

                'location':forms.TextInput(attrs={'class':'form-control'},),


                 }