from django.contrib import admin
from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description', 'description']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    list_editable = ['short_description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'description', 'course', 'order']
    list_display_links = ['subject']
    list_filter = ['subject']
    search_fields = ['subject']
    list_editable = ['description']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
