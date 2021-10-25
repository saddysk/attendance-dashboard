from django.urls import path
from base import views

urlpatterns = [
    path('user-dashboard/', views.userDashboard, name='userDashboard'),
    path('admin-dashboard/', views.adminDashboard, name='adminDashboard'),
]
