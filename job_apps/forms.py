from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['position', 'company', 'location',
                  'post_url', 'contact_name', 'status']
        labels = {'position': 'Title', 'company': 'Company', 'location': 'Location',
                  'post_url': 'Post URL', 'contact_name': 'Contact Name', 'status': 'Status'}
