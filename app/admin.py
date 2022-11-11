"""
Defining the all admin functionalities here.

"""
from django.contrib import admin
from .models import HospitalActor,Treatment,Appointment,OrganDonation

admin.site.register(HospitalActor)
admin.site.register(Treatment)
admin.site.register(Appointment)
admin.site.register(OrganDonation)
