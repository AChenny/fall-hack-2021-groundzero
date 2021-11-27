from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timezone
import pytz


class geolocation(forms.Form):
    # radius
    # address
    RADIUS =forms.CharField(label='radius', initial = "1500")
    ADDRESS = forms.CharField(label='address', required = True)
