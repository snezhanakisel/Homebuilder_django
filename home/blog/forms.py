from django.forms import ModelForm, TextInput
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name, Profession'
            }),
            'message': TextInput(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'message'

            })
        }