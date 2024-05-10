from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .forms import RegisterUserForm
from .models import *
from django.contrib.auth import login, authenticate, logout

# Create your views here.

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def main(request):
    return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не НАЙДЕНА</h1>')

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу после успешной регистрации
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода