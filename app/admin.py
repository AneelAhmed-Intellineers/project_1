from django.contrib import admin


from .models import Student, Grade


admin.site.register(Grade)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'enrollment']