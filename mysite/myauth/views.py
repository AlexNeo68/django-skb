from django.utils.translation import gettext as _, ngettext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import CreateView, TemplateView
from .models import Profile
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# class LoginView(View):
#     def get(self, request:HttpRequest):
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#         return render(request, 'myauth/login.html')
    
#     def post(self, request: HttpRequest):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('/admin/')
        
#         return render(request, 'myauth/login.html', {'error': 'Некорректные имя пользователя или пароль'})


def logout_view(request:HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))


class MyAuthLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('myauth:login')


@user_passes_test(lambda u:u.is_superuser)
def set_cookie_view(request:HttpRequest)->HttpResponse:
    response = HttpResponse('Куки установлены')
    response.set_cookie('fizz', 'bro-value', max_age=3600)
    return response

def get_cookie_view(request:HttpRequest)->HttpResponse:
    value = request.COOKIES.get('fizz', 'default value fizz')
    return HttpResponse(f'Cookie values is: {value}')

@permission_required('myauth.view_profile', raise_exception=True)
def set_session_view(request:HttpRequest)->HttpResponse:
    request.session['alexneo'] = 'sherry'
    return HttpResponse('Сессия сохранена')

@login_required
def get_session_view(request:HttpRequest)->HttpResponse:
    session_value = request.session.get('alexneo', 'default value session')
    return HttpResponse(f'Session value {session_value}')

class ProfileView(TemplateView):
    template_name = 'myauth/about-me.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
    

class MyAuthRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        
        return response

class FooBarView(View):
    def get(self, request):
        return JsonResponse({'foo': 123, 'bar': 456})
    

class HelloWorldTransView(View):
    welcome_message = _('hello my world')

    def get(self, request:HttpRequest):
        items_str = request.GET.get('items') or 0
        items = int(items_str)

        products_line = ngettext(
            "one product",
            "{count} products",
            items,
        )

        products_line = products_line.format(count=items)

        return HttpResponse(
            f'<h1>{self.welcome_message}</h1>'
            f'\n<h2>{products_line}</h1>'
        )