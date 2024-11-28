from django import forms
from .models import ContactFeedback

class ContactFeedbackForm(forms.ModelForm):
    class Meta:
        model = ContactFeedback
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
