from django.shortcuts import render, HttpResponse, redirect
from base import datahandler as data

# Create your views here.


def userDashboard(request):
    userId = "7jB6stkrsnSGoNcEV8HdidPGUhp1"
    userDetails = data.getUserDetails(userId)
    attendance = data.getAttendance(userId)

    context = {
        'userDetails': userDetails
    }
    return render(request, 'user.html', context)


def adminDashboard(request):
    return render(request, 'admin.html')
