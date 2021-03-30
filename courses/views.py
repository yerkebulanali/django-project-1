from django.shortcuts import render
from courses.models import Course, Lesson

def detail_courses(request):
    courses = Course.objects.all()
    return render(request, "courses/detail_lessons.html", {'courses_list': courses})


def detail_lessons(request, pk):
    courses = Course.objects.filter(id=pk)
    lessons = Lesson.objects.filter(course_id=pk)
    return render(request, "courses/detail_courses.html", {'courses_list': courses, 'lessons_list': lessons})

