from django.urls import path

from .views import GroupView, hello_world_view


app_name='myapi'

urlpatterns = [
    path("hello/", hello_world_view, name='api-hello-world'),
    path("groups/", GroupView.as_view(), name='api-groups'), 
]