from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'dob', 'email']
    list_display_links = ['firstname']
    list_filter = ['firstname']
    search_fields = ['firstname']
    list_editable = ['dob']


admin.site.register(Student, StudentAdmin)