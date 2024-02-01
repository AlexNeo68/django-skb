from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.contrib.syndication.views import Feed

from .models import Article

class ArticleListView(ListView):
    model = Article
    queryset = (Article.objects.filter(published_at__isnull=False).order_by('-published_at'))


class ArticleDetailView(DetailView):
    model = Article
    queryset = (Article.objects.filter(published_at__isnull=False))


class ArticleLatestFeed(Feed):
    title = 'Articles latest feed'
    description = 'You see latest artincles on our site'
    link = reverse_lazy('blogapp:article-list')

    def items(self):
        return Article.objects.filter(published_at__isnull=False).order_by('-published_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:200]


