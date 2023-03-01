from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User


from .models import Group, Post

POSTS_PER_PAGE = 10


def index(request):
    title = 'Главная страница проекта Yatube'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

def profile(request, username):
    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author).order_by('-pub_date')
    title = f'Профайл пользователя {author.username}'
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'title': title,
        'page_obj': page_obj,
        'total_posts': post_list.count(),
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    post_number = post.author.posts.count()
    context = {
        'post': post,
        'post_number': post_number,
    }
    return render(request, template, context) 
