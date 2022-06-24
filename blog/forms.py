from django import forms

from .models import blog

class blogForm(forms.Model):

    class Meta:

        model = blog
        fields = [
            'title', 'slug', 'author', 'body',
            'publish', 'created', 'updated', 'status'
        ]