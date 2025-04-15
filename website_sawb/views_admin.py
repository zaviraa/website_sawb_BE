from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from blog.models import Article
from django.core.paginator import Paginator
from blog.forms import ArticleForm

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff: 
            login(request, user)
            return redirect("admin_home")  
        else:
            return render(request, "admin/login.html", {"error": "Invalid credentials or not an admin."})

    return render(request, "admin/login.html")

def admin_logout(request):
    if request.method == "POST":
        logout(request)  
        return redirect('admin-login') 
    return redirect('admin_home') 

def all_articles(request):
    articles_list = Article.objects.all()
    query = request.GET.get('q', '')
    articles_list = Article.objects.filter(title__icontains=query) 
    paginator = Paginator(articles_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all-article.html', {'page_obj': page_obj})

def delete_article(request, id):
    article = get_object_or_404(Article, id=id)

    if request.user.is_authenticated and request.user.is_staff:
        article.delete()
        return redirect('all_articles')
    else:
        return redirect('all_articles')

def edit_article(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()  
            return redirect('all_articles') 
    else:
        form = ArticleForm(instance=article)

    return render(request, 'edit_article.html', {'form': form, 'article': article})

@staff_member_required
def admin_home(request):
    return render(request, "admin/admin_home.html")

@staff_member_required
def admin_dashboard(request):
    return render(request, "admin/dashboard.html") 

@staff_member_required
def admin_blog(request):
    return render(request, "admin/admin_blog.html") 

@staff_member_required
def add_article(request):
    return render(request, "admin/add_article.html")

@staff_member_required
def all_article(request):
    return render(request, "admin/all-article.html")

@staff_member_required
def admin_about(request):
    return render(request, "admin/admin_about.html")

@staff_member_required
def admin_contact(request):
    return render(request, "admin/admin_contact.html")

@staff_member_required
def admin_article(request):
    return render(request, "admin/admin_article.html")

@staff_member_required
def article(request):
    return render(request, "admin/article.html")



