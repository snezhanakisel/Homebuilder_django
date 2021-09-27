from django.forms import ModelForm, Textarea, TextInput
from .models import Contact, Feedback


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput( attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name'
            } ),
            'email': TextInput( attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Your Email'
            } ),
            'message': Textarea( attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Your Message'

            } )
        }

class FeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
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
