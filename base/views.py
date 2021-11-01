from django.shortcuts import render, HttpResponse, redirect
from base import datahandler as data
from django.contrib import messages
from datetime import datetime

# Create your views here.


def userDashboard(request):
    context = {}

    # user's personal details
    userId = "5IrgYvcmWSG1VQlh3S1z"
    userDetails = data.getUserDetails(userId)
    if userDetails is None:
        messages.error(
            request, "Some error occured! Can't get User's personal details.")
        return render(request, 'user.html')
    context['userDetails'] = userDetails

    # get attendance
    if request.method == 'POST':
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']

        if fromDate == "" or toDate == "":
            messages.error(request, "Select both FROM DATE and TO DATE.")
            return render(request, 'user.html', context)
        newFromDate = datetime.strptime(fromDate, "%Y-%m-%d").date()
        newToDate = datetime.strptime(toDate, "%Y-%m-%d").date()
        if newFromDate > newToDate:
            messages.error(
                request, "FROM DATE should be before than TO DATE.")
            return render(request, 'user.html', context)

        attendanceDetails = data.getAttendance(userId, newFromDate, newToDate)
        if attendanceDetails is None:
            messages.error(request, "Some Error occured! Please try again.")
            return render(request, 'user.html', context)
        context['attendance'] = attendanceDetails['attendance']
        context['positivePercent'] = attendanceDetails['positivePercent']
        context['negativePercent'] = attendanceDetails['negativePercent']
        return render(request, 'user.html', context)

    attendanceDetails = data.getAttendance(userId)
    if attendanceDetails is None:
        messages.error(request, "Some Error occured! Please try again.")
        return render(request, 'user.html', context)
    context['attendance'] = attendanceDetails['attendance']
    context['positivePercent'] = attendanceDetails['positivePercent']
    context['negativePercent'] = attendanceDetails['negativePercent']
    return render(request, 'user.html', context)


def adminDashboard(request):
    context = {}

    # admin's personal details
    adminId = "5IrgYvcmWSG1VQlh3S1z"
    adminDetails = data.getUserDetails(adminId)
    if adminDetails is None:
        messages.error(
            request, "Some error occured! Can't get User's personal details.")
        return render(request, 'user.html')
    context['adminDetails'] = adminDetails

    # get attendance - SCHOOL Wise
    if request.method == 'POST':
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']

        if fromDate == "" or toDate == "":
            messages.error(request, "Select both FROM DATE and TO DATE.")
            return render(request, 'admin.html', context)
        newFromDate = datetime.strptime(fromDate, "%Y-%m-%d").date()
        newToDate = datetime.strptime(toDate, "%Y-%m-%d").date()
        if newFromDate > newToDate:
            messages.error(
                request, "FROM DATE should be before than TO DATE.")
            return render(request, 'admin.html', context)

        individualAttendance = data.getIndividualAttendance(
            newFromDate, newToDate)
        if individualAttendance is None:
            messages.error(request, "Some Error occured! Please try again.")
            return render(request, 'admin.html', context)

        context['individualAttendance'] = individualAttendance
        print('\n\n*-*************', individualAttendance)
        return render(request, 'admin.html', context)
    return render(request, 'admin.html', context)
