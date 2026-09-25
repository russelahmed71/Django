from django.urls import path
from management import views

urlpatterns = [
    path('', views.addStudent, name='addStudent'),
    path('student/call/<int:id>/', views.studentIdCall, name='studentIdCall'),
    path('student/update/', views.updateStudent, name='updateStudent'),
    path('student/delete/<int:id>/', views.deleteStudent, name='deleteStudent'),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logoutView, name='logoutView'),
    path('change-password/', views.changePassword, name='changePassword'),
]
