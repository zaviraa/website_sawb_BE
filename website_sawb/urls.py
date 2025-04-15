from django.contrib import admin
from django.urls import path, include
from website_sawb import views as user_views
from website_sawb import views_admin
from django.conf import settings
from django.conf.urls.static import static
from blog.views import ArticleViewSet
from .import views


urlpatterns = [
    # URL untuk User
    path('', user_views.index, name='index'),
    path('about/', user_views.about, name='about'),
    path('contact/', user_views.contact, name='contact'),
    path('blog/', user_views.blog, name='blog'),

    # Django Admin Default
    path('admin/', admin.site.urls), 
    path('api/', include('api.urls')),
    path('article/<int:pk>/publish/', ArticleViewSet.as_view({'post': 'publish'}), name='article_publish'),


    # URL untuk Admin
    path('admin-login/', views_admin.admin_login, name='admin-login'),
    path('admin-logout/', views_admin.admin_logout, name='admin-logout'),
    path('admin-dashboard/', views_admin.admin_dashboard, name='admin-dashboard'),
    path('admin-home/', views_admin.admin_home, name='admin_home'),
    path('admin-blog/', views_admin.admin_blog, name='admin_blog'),
    path('admin-about/', views_admin.admin_about, name='admin_about'),
    path('admin-contact/', views_admin.admin_contact, name='admin_contact'),
    path('admin-dashboard/article/', views_admin.article, name='article'),
    path('admin-dashboard/admin_article/', views_admin.admin_article, name='admin_article'),
    path('admin-dashboard/add_article/', views_admin.add_article, name='add_article'),
    path('admin-dashboard/all-article/', views_admin.all_article, name='all-article'),
    path('article/<int:id>/', views_admin.admin_article, name='admin_article'),
    path('edit_article/<int:id>/', views_admin.add_article, name='edit_add_article'),
    path('delete_article/<int:id>/', views_admin.delete_article, name='delete_article'),
]

urlpatterns += static(settings.STATIC_URL, document_root=getattr(settings, 'STATICFILES_DIRS', [settings.STATIC_ROOT])[0])