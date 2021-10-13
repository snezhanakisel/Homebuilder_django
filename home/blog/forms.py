from django.forms import ModelForm, TextInput, HiddenInput
from .models import Comment, Post


# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['author', 'message', 'post']
#         widgets = {
#             'author': HiddenInput(attrs={
#                 'class': 'form-control',
#                 'id': 'name',
#                 'placeholder': 'Your Name, Profession'
#             }),
#             'message': TextInput(attrs={
#                 'class': 'form-control',
#                 'id': 'message',
#                 'placeholder': 'message'
#
#             }),
#             'post': HiddenInput(attrs={
#                 'class': 'form-control',
#                 'id': 'post',
#                 'placeholder': 'post'
#         })
#         }