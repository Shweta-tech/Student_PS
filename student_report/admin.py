from django.contrib import admin

from .models import Student_detail,subject,mark

admin.site.register(Student_detail)
admin.site.register(subject)

admin.site.register(mark)

# Register your models here.
