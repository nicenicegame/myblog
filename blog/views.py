from django.shortcuts import render, redirect
from .models import Post
from .forms import LoginForm, SignupForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'blog/home.html',)


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {
        'posts': posts,
        'nav': 'all_posts'
    })


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/detail.html', {
        'post': post
    })


@login_required(login_url='/login')
def create_post(request):
    if not request.user.is_authenticated:
        return Http404
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid:
            post = Post(
                post_content=request.POST['post_content'],
                post_title=request.POST['post_title'],
                author=request.user
            )
            post.save()
            return redirect('posts')
    else:
        post_form = PostForm()
    return render(request, 'blog/new.html', {'post_form': post_form})


@login_required(login_url='/login')
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts')


@login_required(login_url='/login')
def edit_post(request):
    pass


def signup_page(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()
            return redirect('login')
        else:
            return render(request, 'blog/signup.html', {
                'nav': 'signup',
                'signup_form': signup_form
            })

    else:
        signup_form = SignupForm()
    return render(request, 'blog/signup.html', {
        'nav': 'signup',
        'signup_form': signup_form
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(username, password)
        if login_form.is_valid:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                login_form = LoginForm()
    else:
        login_form = LoginForm()
    return render(request, 'blog/login.html', {
        'nav': 'login',
        'login_form': login_form,
    })


def logout_user(request):
    logout(request)
    return redirect('index')
