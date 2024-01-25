
from django.urls import path
from .views import *

app_name='shopapp'

urlpatterns = [
    path("", index, name='shopapp-index'),
]