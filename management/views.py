from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class DashboardView(LoginRequiredMixin, SuccessMessageMixin, CreateView, ListView):
    model = Student
    template_name = 'add_student.html'
    fields = ['name', 'roll', 'semester', 'department', 'profile_pic']
    context_object_name = 'students'
    success_url = reverse_lazy('addStudent')
    success_message = "Student record added successfully!"
    login_url = 'loginView'

class StudentEditCallView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = ['name', 'roll', 'semester', 'department', 'profile_pic']
    login_url = 'loginView'

class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = ['name', 'roll', 'semester', 'department', 'profile_pic']
    success_url = reverse_lazy('addStudent')
    success_message = "Student record updated successfully!"
    login_url = 'loginView'
class StudentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('addStudent')
    success_message = "Student record deleted successfully!"
    login_url = 'loginView'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = "Welcome back!"

class UserLogoutView(LogoutView):
    next_page = 'loginView'

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('addStudent')
    success_message = "Your password was successfully updated!"