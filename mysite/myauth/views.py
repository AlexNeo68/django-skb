from django.contrib.auth import authenticate, login
from django.http import HttpRequest
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
