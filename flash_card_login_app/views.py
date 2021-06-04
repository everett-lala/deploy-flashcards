from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
#added for ajax
from django.http import JsonResponse


def index(request):
    return render(request, 'authentication/login.html')


def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['username'] = user.username
        request.session['greeting'] = user.first_name
        messages.info(request, "User registered; You can now log in.")
        return redirect('/')


def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(username=request.POST['login_username'])
        request.session['username'] = user.username
        request.session['greeting'] = user.first_name
        context = {
            'this_user': User.objects.get(username=request.session['username']),
        }
        print(User.objects.get(username=request.session['username']))
        return redirect('/flashcards')


def logout(request):
    request.session.flush()
    return redirect('/')



########################### ADDED for AJAX ######################################
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    return JsonResponse(data)