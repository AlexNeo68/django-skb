from django.urls import path
from .views import get_cookie_view, set_cookie_view, set_session_view, get_session_view, MyAuthLogoutView, logout_view
from django.contrib.auth import views as auth_views

app_name='myauth'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='myauth/login.html', redirect_authenticated_user=True), name='login'),
    # path("login/", LoginView.as_view(), name='login'),
    path('set-cookie/', set_cookie_view, name='set-cookie'),
    path('get-cookie/', get_cookie_view, name='get-cookie'),
    path('get-session/', get_session_view, name='get-session'),
    path('set-session/', set_session_view, name='set-session'),
    # path('logout/', MyAuthLogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
]