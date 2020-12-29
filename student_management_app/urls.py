
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.loginPage, name="login"),
   
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),



    path('student_home/', views.student_home, name="student_home"),
    path('student_view_attendance/', views.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', views.student_view_attendance_post, name="student_view_attendance_post"),
   
    path('student_feedback/', views.student_feedback, name="student_feedback"),
    path('student_feedback_save/', views.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', views.student_profile, name="student_profile"),
    path('student_profile_update/', views.student_profile_update, name="student_profile_update"),
    path('student_view_result/', views.student_view_result, name="student_view_result"),
    path('student_assignments/',views.student_assignments,name="student_assignments"),
    path('student_mental_health/',views.student_mental_health,name="student_mental_health"),
]
