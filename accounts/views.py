from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from accounts.models import UserAccount, AdminAccount
# import hashlib

# Create your views here.


# Login
def userLogin(request):
    return render(request, 'userlogin.html')


def adminLogin(request):
    return render(request, 'adminlogin.html')


# Logout
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('userLogin')
    else:
        return redirect('userLogin')


def adminLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('adminLogin')
    else:
        return redirect('adminLogin')
