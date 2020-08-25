from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from todo_app import views


@csrf_exempt
def create_user(request):
    return render(request, 'users/register.html')


@csrf_exempt
def login_user(request):
    return render(request, 'users/login.html')


@csrf_exempt
def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST':
        User.objects.create_user(name, email, password)
        return redirect(login)
    return redirect(login)


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        return redirect(views.tasks_todo)
    if user is None:
        return redirect(register)