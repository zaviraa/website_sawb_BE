from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from .forms import ArticleForm
from django.utils import timezone
from django.contrib import messages


def blog_index(request):
    featured_article = Article.objects.filter(is_featured=True).first()
    articles = Article.objects.order_by('-published_at')[:4]
    return render(request, 'user/index.html', {
        'featured_article': featured_article,
        'articles': articles
    })

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            if article.status == Article.PUBLISHED and not article.published_at:
               article.published_at = timezone.now()
            article.save()

            messages.success(request, 'Artikel berhasil terbit.') 
            return redirect('all_article')
        else:
            print("Form tidak valid:", form.errors)
            messages.error(request, 'Gagal menambahkan artikel. Periksa form dan coba lagi.')
    else:
        form = ArticleForm()
    categories = Category.objects.all()
    return render(request, 'add_article.html', {
        'form': form,
        'categories': categories
    })
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def articles(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        articles = Article.objects.filter(category=category)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        if article.status == 'published':
            return Response({'status': 'Artikel sudah diterbitkan sebelumnya.'}, status=status.HTTP_400_BAD_REQUEST)
        
        article.publish()
        return Response({'status': 'Artikel berhasil diterbitkan.'}, status=status.HTTP_200_OK)