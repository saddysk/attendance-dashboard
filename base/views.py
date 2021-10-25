from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def userDashboard(request):
    return render(request, 'user.html')


def adminDashboard(request):
    return render(request, 'admin.html')
