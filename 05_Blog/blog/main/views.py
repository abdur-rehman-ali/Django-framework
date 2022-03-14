from dataclasses import fields
from statistics import mode
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

class postDetail(DetailView):
    model = Post
    template_name = 'updatePost.html'

class postCreate(CreateView):
    model = Post
    template_name = 'createPost.html'
    fields = ['title','description','author']
    success_url = reverse_lazy('index')
