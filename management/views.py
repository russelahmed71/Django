from django.shortcuts import render, redirect, get_object_or_404 # <-- Added get_object_or_404 here
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student


@login_required(login_url='loginView') 
def addStudent(request):
    if request.method == "POST":
        s_name = request.POST.get('name')
        s_roll = request.POST.get('roll')
        s_semester = request.POST.get('semester')
        s_department = request.POST.get('department')
        s_image = request.FILES.get('profile_pic')

        new_student = Student(
            name=s_name,
            roll=s_roll,
            semester=s_semester,
            department=s_department,
            profile_pic=s_image
        )
        new_student.save()
        messages.success(request, "Student record added successfully!")
        return redirect('addStudent')

    students = Student.objects.all()
    return render(request, 'add_student.html', {'students': students})


@login_required(login_url='loginView')
def studentIdCall(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'update_student.html', {'student': student})


@login_required(login_url='loginView')
def updateStudent(request):
    if request.method == "POST":
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.semester = request.POST.get('semester')
        student.department = request.POST.get('department')
        
        new_image = request.FILES.get('profile_pic')
        if new_image:
            student.profile_pic = new_image  

        student.save()
        messages.success(request, "Student record updated successfully!")
        
    return redirect('addStudent')


@login_required(login_url='loginView')
def deleteStudent(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Student record deleted successfully!")
    return redirect('addStudent')



def loginView(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        
        user = authenticate(request, username=uname, password=upass)
        
        if user is not None:
            login(request, user)
            return redirect('addStudent')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('loginView')
            
    return render(request, 'login.html')


def logoutView(request): 
    logout(request)
    return redirect('loginView')


@login_required(login_url='loginView')
def changePassword(request):
    if request.method == "POST":
        old_pass = request.POST.get('old_password')
        new_pass = request.POST.get('new_password')
        confirm_pass = request.POST.get('confirm_password')
        
        user = request.user
        
        if not user.check_password(old_pass):
            messages.error(request, "Your current password was entered incorrectly.")
            return redirect('changePassword')
            
        if new_pass != confirm_pass:
            messages.error(request, "The two new password fields didn't match.")
            return redirect('changePassword')
            
        user.set_password(new_pass)
        user.save()
        
        update_session_auth_hash(request, user)
        messages.success(request, "Your password was successfully updated!")
        return redirect('addStudent')
        
    return render(request, 'change_password.html')
