from django import forms
from .models import PlannedRoute

class PlannedRouteForm(forms.ModelForm):
    class Meta:
        model = PlannedRoute
        fields = ['starting_location', 'finishing_location', 'with_who', 'time_limit', 'pin_code', 'additional_info']
        widgets = {
            'starting_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter starting location',
            }),
            'finishing_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter finishing location',
            }),
            'with_who': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter companions or who you plan to meet(e.g., John, Jane)',
            }),
            'time_limit': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter timer limit in minutes',
            }),
            'pin_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter an AlphaNumeric PIN code (max 10 characters)',
            }),
            'additional_info': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any additional information that could be helpful in case of an emergency',
                'rows': 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Required fields
        self.fields['starting_location'].required = True
        self.fields['finishing_location'].required = True
        self.fields['with_who'].required = True
        self.fields['time_limit'].required = True
        self.fields['pin_code'].required = True  
        self.fields['additional_info'].required = False

    def clean_time_limit(self):
        time_limit = self.cleaned_data.get('time_limit')
        if time_limit <= 0:
            raise forms.ValidationError("Time limit must be a positive number.")
        return time_limit