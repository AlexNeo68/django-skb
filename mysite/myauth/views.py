from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

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


def set_cookie_view(request:HttpRequest)->HttpResponse:
    response = HttpResponse('Куки установлены')
    response.set_cookie('fizz', 'bro-value', max_age=3600)
    return response

def get_cookie_view(request:HttpRequest)->HttpResponse:
    value = request.COOKIES.get('fizz', 'default value fizz')
    return HttpResponse(f'Cookie values is: {value}')


def set_session_view(request:HttpRequest)->HttpResponse:
    request.session['alexneo'] = 'sherry'
    return HttpResponse('Сессия сохранена')

def get_session_view(request:HttpRequest)->HttpResponse:
    session_value = request.session.get('alexneo', 'default value session')
    return HttpResponse(f'Session value {session_value}')

