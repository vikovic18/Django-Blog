from re import template
from django.shortcuts import render
from django.views import generic

from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostListView(generic.ListView):
    model=  Post
    template_name = 'post_list.html'

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = 'post_form.html'
    success_url  = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model: Post
    template_name = 'post_detail.view'

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = 'base.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = 'post_confirm_delete.html'