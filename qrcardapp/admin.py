from django.contrib import admin

# Register your models here.

from .models import Profile, Qualifications, InstructionalCourses, LeaveDetails, ServiceRecords, EmploymentDetails

admin.site.site_header = "Humanitarian Peace Support School"
admin.site.site_title = "Humanitarian Peace Support School"
admin.site.index_title = "Administration"
admin.AdminSite.index_title = "ADMIN DASHBOARD"


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('service_number', )
    list_display = ('service_number', 'rank', 'unit', 'sub_unit', 'ROD', 'phone_number', )
    list_display_links = ('service_number', 'rank', 'unit', 'sub_unit',)


class QualificationsAdmin(admin.ModelAdmin):
    pass


class InstructionalCoursesAdmin(admin.ModelAdmin):
    pass


class LeaveDetailsAdmin(admin.ModelAdmin):
    pass


class ServiceRecordsAdmin(admin.ModelAdmin):
    pass


class EmploymentDetailsAdmin(admin.ModelAdmin):
    search_fields = ('service_number', )
    list_display = ('service_number', 'terms_of_service', 'date_of_engagement', 'run_out_date',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Qualifications, QualificationsAdmin)
admin.site.register(InstructionalCourses, InstructionalCoursesAdmin)
admin.site.register(LeaveDetails, LeaveDetailsAdmin)
admin.site.register(ServiceRecords, ServiceRecordsAdmin)
admin.site.register(EmploymentDetails, EmploymentDetailsAdmin)
