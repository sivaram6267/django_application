from django.contrib import admin
from testapp.models import HydJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)
