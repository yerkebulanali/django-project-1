"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from quadratic.views import quadratic_results
from courses.views import detail_courses, detail_lessons
from students.views import course_students_list, students_list, detail

urlpatterns = [
    path('', detail_courses),
    path('courses/<int:pk>/', detail_lessons),
    path('students/', students_list),
    path('coursestudents/<int:pk>/', course_students_list),
    path('students/<int:pk>/', detail),
    path('quadratic/results/', quadratic_results),
    path('admin/', admin.site.urls),
]
