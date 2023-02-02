from .models import comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('content',)