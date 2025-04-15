from django.shortcuts import render
from blog.models import Article

def index(request):
    return render(request, 'user/index.html')

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    return render(request, 'user/contact.html')

def blog(request):
    return render(request, 'user/blog.html')

def blog_index(request):
    featured_article = Article.objects.filter(is_featured=True, status='published').first()
    articles = Article.objects.filter(status='published').order_by('-published_at')[:4]
    return render(request, 'blog/index.html', {
        'featured_article': featured_article,
        'articles': articles
    })
