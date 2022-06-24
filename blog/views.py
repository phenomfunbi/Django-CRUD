from re import template
from django.views.generic.edit import CreateView
from .models import blog

class blogCreateView(CreateView):
    model = blog
    fields = [
        'title', 'slug', 'author', 'body',
         'publish', 'created', 'updated', 'status'
    ]
template_name = 'home.html'