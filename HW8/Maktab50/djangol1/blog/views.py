from django.shortcuts import render
from . import models


def show_all_posts(request):

    my_posts = models.Post.objects.all()
    return render(
        request,
        context={'my_posts': my_posts},
        template_name='blog/all_posts.html'
    )
