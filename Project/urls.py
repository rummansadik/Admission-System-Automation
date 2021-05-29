from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from login_system.views import home

urlpatterns = [
    path('', home, name='home_page'),
    path('login/student',
         LoginView.as_view(template_name='student/login.html'),
         name='student_login'),
    path('login/teacher',
         LoginView.as_view(template_name='teacher/login.html'),
         name='teacher_login'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
