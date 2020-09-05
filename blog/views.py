from django.shortcuts import render, redirect
from .models import Post
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'blog/home.html',)


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {
        'posts': posts,
        'nav': 'all_posts'
    })


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
