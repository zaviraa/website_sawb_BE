from django.contrib import admin
from .models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'author')
    list_filter = ('category',)
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
