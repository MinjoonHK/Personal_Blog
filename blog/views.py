from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
# Create your views here.
