from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'first_name', 'last_name']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set fields as required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone_number'].required = True