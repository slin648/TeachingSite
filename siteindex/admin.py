from django.contrib import admin
from .models import Lecturer, Lesson, Syllabus,  Record

# Register your models here.


admin.site.register(Syllabus)
admin.site.register(Record)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'college')


admin.site.register(Lecturer, LecturerAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer', 'date_of_release')

    fieldsets = (
        ('属性', {
            'fields': ('title', 'precondition', 'lecturer', 'summary', 'date_of_release')
        }),
        ('内容', {
            'fields': ('video', 'image_1', 'parag_1', 'image_2', 'parag_2', 'image_3', 'parag_3')
        }),
    )


admin.site.register(Lesson, LessonAdmin)
