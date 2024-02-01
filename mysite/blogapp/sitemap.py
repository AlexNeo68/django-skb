from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.filter(published_at__isnull=False).order_by('-published_at')

    def lastmod(self, obj):
        return obj.published_at