from django.urls import path
from .views import *

app_name='requestapp'

urlpatterns = [
    path("", index, name='req-index'),
    path("handle-post/", handle_post, name='req-post'),
    path("handle-file/", handle_file, name='req-file'),
]