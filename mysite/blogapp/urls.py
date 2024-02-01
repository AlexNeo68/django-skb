from django.urls import path
from .views import ArticleDetailView, ArticleLatestFeed, ArticleListView

app_name="blogapp"

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('feed/', ArticleLatestFeed(), name='article-feed'),
]