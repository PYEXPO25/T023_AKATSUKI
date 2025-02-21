from django import forms
from .models import bill_Data

class RoomForm(forms.ModelForm):
    class Meta:
        model = bill_Data
        fields = ['room_number', 'rent', 'electricity', 'water', 'food', 'parking']

