from django.urls import path
from accounts import views

urlpatterns = [
    path('user-login/', views.userLogin, name='userLogin'),
    path('admin-login/', views.adminLogin, name='adminLogin'),

    path('user-logout/', views.userLogout, name='userLogout'),
    path('admin-logout/', views.adminLogout, name='adminLogout'),
]
