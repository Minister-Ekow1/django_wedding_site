from django import forms
from .models import GuestMessage

class GuestMessageForm(forms.ModelForm):
    class Meta:
        model = GuestMessage
        fields = ['name', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }