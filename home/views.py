from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Post
from django.http import JsonResponse

class MainView(TemplateView):
    template_name = 'main.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper - 3 
        posts = list(Post.objects.values()[lower:upper])
        posts_size = len(Post.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)