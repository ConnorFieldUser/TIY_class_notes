
from django import forms
from app.models import Chirp


class ChirpForm(forms.ModelForm):

    class Meta:
        fields = ("body", )
        model = Chirp
