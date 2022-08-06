import imp
from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from.forms import StudentUserForm,StudentExtraForm,TeacherUserForm,TeacherExtraForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from.models import student,teacher
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def home(request):
    return render(request,'lms/home.html')
def studentlogin(request):
    User = get_user_model()
    if request.method=='POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            
            return redirect('/success')
    else:
        return render(request,'lms/student_login.html')
def teacherlogin(request):
    User = get_user_model()
    if request.method=='POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            
            return redirect('/tsuccess')
    else:
        return render(request,'lms/teacher_login.html')
def studentsignup_view(request):
    User = get_user_model()
    form1=StudentUserForm()
    form2=StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=StudentUserForm(request.POST)
        form2=StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.is_student=True
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

           

        return redirect('/student_login')
    return render(request,'lms/studentsignup.html',context=mydict)
def teachersignup_view(request):
    User = get_user_model()
    form1=TeacherUserForm()
    form2=TeacherExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=TeacherUserForm(request.POST)
        form2=TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.is_teacher=True
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

           

        return redirect('/teacher_login')
    return render(request,'lms/teachersignup.html',context=mydict)
@login_required(login_url='student_login/')
def studentsuccess(request):
    current_user=request.user
    id=current_user.id
    obj=student.objects.get(pk=id)
    print(obj)
    return render(request,'lms/studentprofile.html',{"obj":obj})
@login_required(login_url='tlogin')
def teachersuccess(request):
    current_user=request.user
    id=current_user.id
    obj=teacher.objects.get(pk=id)
    print(obj)
    return render(request,'lms/teacherprofile.html',{"obj":obj})