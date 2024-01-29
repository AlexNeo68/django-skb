from django.urls import path

from .views import hello_world_view


app_name='myapi'

urlpatterns = [
    path("hello/", hello_world_view, name='api-hello-world') 
]