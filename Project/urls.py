from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from login_system.views import home, student_register, teacher_register


urlpatterns = [
    path('', home, name='home_page'),
    path('register/student',
         student_register, name='student_register'),
    path('login/student',
         LoginView.as_view(template_name='student/login.html'),
         name='student_login'),
    path('logout/student',
         LogoutView.as_view(template_name='student/logout.html'),
         name='student_logout'),
    path('register/teacher',
         teacher_register, name='teacher_register'),
    path('login/teacher',
         LoginView.as_view(template_name='teacher/login.html'),
         name='teacher_login'),
    path('logout/teacher',
         LogoutView.as_view(template_name='teacher/logout.html'),
         name='teacher_logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
