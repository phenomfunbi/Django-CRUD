from re import template
from django.views.generic.edit import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        'title', 'slug', 'author', 'body',
         'publish', 'created', 'updated', 'status'
    ]
template_name = 'home.html'