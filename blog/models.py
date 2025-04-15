from django.db import models
from django.utils import timezone

class Category(models.Model):
    POLITIK = 'POLITIK'
    SOSIAL = 'SOSIAL'
    PERTEMUAN = 'PERTEMUAN'

    CATEGORY_CHOICES = [
        (POLITIK, 'Politik'),
        (SOSIAL, 'Sosial'),
        (PERTEMUAN, 'Pertemuan'),
    ]

    name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, default='Admin')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    published_at = models.DateTimeField(null=True, blank=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    is_featured = models.BooleanField(default=False) 

    def publish(self):
        self.status = self.PUBLISHED
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
