from django.urls import path
# from .views import *
from django.contrib.auth import views as auth_views

app_name='myauth'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='myauth/login.html', redirect_authenticated_user=True), name='login'),
    # path("login/", LoginView.as_view(), name='login'),
]