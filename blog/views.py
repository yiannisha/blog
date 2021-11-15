from django.shortcuts import render
from .models import Category, Post, Comment
from .forms import CommentForm
# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    # categories for navbar
    nav_categories = Category.objects.all()
    context = {
        'posts' : posts,
        'nav_cats' : nav_categories,
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')

    # categories for navbar
    nav_categories = Category.objects.all()
    context = {
        'posts' : posts,
        'category' : category,
        'nav_cats' : nav_categories,
    }
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()

    form = CommentForm()
    nav_categories = Category.objects.all()
    context = {
        'post' : post,
        'comments' : comments,
        'form' : form,
        'nav_cats' : nav_categories,
    }
    return render(request, 'blog_detail.html', context)
