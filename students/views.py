from django.shortcuts import render
from students.models import Student
from courses.models import Course

def course_students_list(request, pk):
    courses = Course.objects.filter(id=pk)
    students = Student.objects.filter(courses=pk)
    return render(request, "students/course_students_list.html", {'courses_list': courses, 'course_students': students})

def students_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {'students_list': students})

def detail(request, pk):
    student = Student.objects.filter(id=pk)
    courses = Student.objects.get(id=pk).courses.all()
    return render(request, "students/detail.html", {'student': student, 'courses': courses})

