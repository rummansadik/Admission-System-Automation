from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from login_system.views import (
    home, student_register, teacher_register, profile)

urlpatterns = [
    # Home Page
    path('', home, name='home_page'),

    # Student URL
    path('student/register/', student_register, name='student_register'),
    path('student/login/',
         LoginView.as_view(template_name='student/login.html'),
         name='student_login'),

    # Teacher URL
    path('teacher/register/', teacher_register, name='teacher_register'),
    path('teacher/login/',
         LoginView.as_view(template_name='teacher/login.html'),
         name='teacher_login'),

    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
