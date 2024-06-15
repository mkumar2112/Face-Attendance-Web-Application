from django.contrib import admin
from .models import Contacts, EmployeeDetails, Attendance

# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display=['First_Name', 'Email']

class EmplyeeAdmin(admin.ModelAdmin):
    list_display=['Emp_id','Name', 'Email']

class AttendanceAdmin(admin.ModelAdmin):
    list_display=['Emp_id', 'Date', 'Time']


admin.site.register(Contacts, contactAdmin)
admin.site.register(EmployeeDetails, EmplyeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
# AdminSite.site_title()