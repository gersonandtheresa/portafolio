from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


from django.contrib.auth import get_user_model

@login_required(login_url="login")
def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts,}
    return render(request, 'home.html', context )


def activo(request):
    User = get_user_model()
    gerson = User.objects.get(username='framework2')
    isauri = User.objects.get(username='Isauri')
    context = {'gerson':gerson,'isauri':isauri }
    return render(request, 'home.html', context)

@login_required(login_url="login")
def post_new(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'post_new.html', context)
