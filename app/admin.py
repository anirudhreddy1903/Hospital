from django.contrib import admin
from .models import HospitalActor,Treatment,Appointment,OrganDonation
from import_export.admin import ImportExportModelAdmin

class HospitalActorAdmin(ImportExportModelAdmin):
    list_display = ('pk','username','email','last_name','first_name')
    search_fields = ('last_name','first_name',)
    class Meta:
        model = HospitalActor

class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ('pk','doctor','patient','category','treatment_date',)
    search_fields = ('notes',)
    class Meta:
        model = Treatment


class OrganDonationAdmin(ImportExportModelAdmin):
    list_display = ('pk','last_name','first_name','email','mobile_number','organ_type')
    search_fields = ('last_name','first_name')
    list_filter = ('organ_type',)
    class Meta:
        model = OrganDonation

admin.site.register(HospitalActor,HospitalActorAdmin)
admin.site.register(Treatment,TreatmentAdmin)
admin.site.register(Appointment)
admin.site.register(OrganDonation,OrganDonationAdmin)
