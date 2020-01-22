"""online_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from instructor import views as ins_views
from student import views as st_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('', include('home.urls')),

    path('login/', user_views.login_view, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('profile/', user_views.profile, name="profile"),

    path('instructor/', ins_views.instructor, name="instructor"),
    path('instructor/create_quiz/', ins_views.create_quiz, name="create_quiz"),
    path('instructor/display_questions/', ins_views.display_questions, name="display_questions"),
    path('instructor/view_scores/', ins_views.view_scores, name="view_scores"),

    path('student/', st_views.student, name="student"),
    path('student/start_quiz/', st_views.start_quiz, name="start_quiz"),
    path('student/user_scores/', st_views.user_scores, name="user_scores"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
