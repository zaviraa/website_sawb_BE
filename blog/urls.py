from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet, blog_index
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import views_admin

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', blog_index, name='blog_home'),
    path('api/', include(router.urls)),
    path('add-article/', views.add_article, name='add_article'),
     path('admin-dashboard/all-article/', views_admin.all_article, name='all-article'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
