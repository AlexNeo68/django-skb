from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("blogapp:article-detail", kwargs={"pk": self.pk})
    
    
