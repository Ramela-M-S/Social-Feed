from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.

@login_required
def menu_view(request):
    return render(request, "posts/menu.html")
@login_required
def create_view(request):
    if request.method == "POST":
        form =  PostForm(request.POST ,request.FILES )
        if form.is_valid():
            post =form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("menu")
    else:
        form = PostForm()
    return render(request,"posts/create_post.html", {"form":form})

@login_required
def my_posts(request):
    post = Post.objects.filter(user = request.user).order_by('-created_at')
    return render(request, "posts/my_post.html",{"posts":post})

@login_required
def all_posts(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, "posts/my_post.html",{"posts":post})