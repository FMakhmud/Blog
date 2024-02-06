from django.shortcuts import render, get_object_or_404
from .models import Profile, About, Skill, Portfolio, Post


def index(request):
    profile = Profile.objects.first()
    about = About.objects.all()
    tools = Skill.objects.all()
    context = {"profile": profile, "about": about, "tools": tools}

    return render(request, template_name="index.html", context=context)


def about_me(request):
    tools = Skill.objects.all()
    context = {"tools": tools}

    return render(request, template_name="about-us.html", context=context)


def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {"portfolios": portfolios}

    return render(request, 'portfolio.html', context)


def blog(request):
    posts = Post.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            posts = posts.filter(title__icontains=search)

    return render(request, 'blog.html', {"posts": posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render(request, 'single-blog.html', {"post": post})
