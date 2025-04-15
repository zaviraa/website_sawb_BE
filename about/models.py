from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_us/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class VisionMission(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else f"Gallery Image {self.id}"
