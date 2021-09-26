from django.forms import ModelForm, Textarea, TextInput
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput( attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Name'
            } ),
            'email': TextInput( attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'name@example.com'
            } ),
            'subject': TextInput( attrs={
                'class': 'form-control',
                'id': 'subject',
                'placeholder': 'Subject'

            } ),
            'message': Textarea( attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Message'

            } )
        }
