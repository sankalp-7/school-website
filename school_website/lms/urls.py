from django.urls import path
from.views import home,studentlogin,teacherlogin,studentsignup_view,studentsuccess,teachersignup_view,teachersuccess,viewstudents,logout1,logout
app_name='lms'

urlpatterns=[ 
    path('',home,name='home'),
    path('student_login/',studentlogin,name='slogin'),
    path('teacher_login/',teacherlogin,name='tlogin'),
    path('studentsignup/',studentsignup_view,name='studentsignup'),
    path('teachersignup/',teachersignup_view,name='teachersignup'),
    path('success/',studentsuccess,name='ssuccess'),
    path('tsuccess/',teachersuccess,name='tsuccess'),
    path('logout/',logout,name='logout'),
     path('logout1/',logout1,name='logout1'),
     path('viewstudents/',viewstudents,name='view'),
]
