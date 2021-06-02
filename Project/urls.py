from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from login_system.views import home, student_register, teacher_register, student_profile, teacher_profile


urlpatterns = [
    path('', home, name='home_page'),

    path('student/profile', student_profile, name='student_profile'),
    path('student/register', student_register, name='student_register'),
    path('student/login', LoginView.as_view(template_name='student/login.html'),
         name='student_login'),
    path('student/logout', LogoutView.as_view(template_name='student/logout.html'),
         name='student_logout'),

    path('teacher/profile', teacher_profile, name='teacher_profile'),
    path('teacher/register', teacher_register, name='teacher_register'),
    path('teacher/login', LoginView.as_view(template_name='teacher/login.html'),
         name='teacher_login'),
    path('teacher/logout', LogoutView.as_view(template_name='teacher/logout.html'),
         name='teacher_logout'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
