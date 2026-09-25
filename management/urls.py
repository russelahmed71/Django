from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='addStudent'),
    path('student/edit/<int:pk>/', views.StudentEditCallView.as_view(), name='studentIdCall'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='updateStudent'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='deleteStudent'),
    path('login/', views.UserLoginView.as_view(), name='loginView'),
    path('logout/', views.UserLogoutView.as_view(), name='logoutView'),
    path('password/', views.UserPasswordChangeView.as_view(), name='changePassword'),
]
