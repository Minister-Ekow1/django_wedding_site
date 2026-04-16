from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'attending': forms.Select(
                choices=[(True, 'Yes'), (False, 'No')],
                attrs={'class': 'form-control'}
            ),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'dietary_preferences': forms.TextInput(attrs={'class': 'form-control'}),
        }