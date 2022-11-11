from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings as SETTINGS

PERSON_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

DOCTOR_CATEGORIES = (
    ('PED','Pediatrician'),
    ('CAR','Cardiologist'),
    ('ONC','Oncologist'),
    ('GAS','Gastroenterologist'),
    ('PUL','Pulmonologist'),
    ('END','Endocrinologist'),
    ('OPH','Ophthalmologist'),
    ('DER','Dermatologist'),
    ('NEU','Neurologist'),
    ('RAD','Radiologist'),
    ('SUR','Surgeon'),
    ('PAT','Patient')
)

US_STATES = (
    ('AL','Alabama'),
('AK','Alaska'),('AZ','Arizona'),('AR','Arkansas'),('CA','California'),('CO','Colorado'),('CT','Connecticut'),('DE','Delaware'),('FL','Florida'),('GL','Georgia'),('HI','Hawaii'),('IL','Illinois'),('KS','Kansas'),('MD','Maryland'),
('NY','New York'),('ND','North Dakota'),('TX','Texas'),('VA','Virginia'),('MO','Missouri'),('MI','Michigan'),('NJ','New Jersey'),('WI','	Wisconsin'),('WY','Wyoming')



)

class HospitalActor(AbstractUser):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=60,null=True,blank=True)
    first_name = models.CharField(max_length=60,null=True,blank=True)
    mobile_number = models.CharField(max_length=12,null=True,blank=True)
    gender = models.CharField(max_length=1,choices=PERSON_CHOICES,null=True,blank=True)
    address1 = models.CharField(max_length=30, null=True, blank=True)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    apt_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2,choices=US_STATES, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    category = models.CharField(max_length=3,choices=DOCTOR_CATEGORIES,null=True,blank=True)
    is_patient = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)


# class Patient(AbstractUser):
#     patient_id = models.AutoField(primary_key=True)
#     last_name = models.CharField(max_length=60,null=True,blank=True)
#     first_name = models.CharField(max_length=60,null=True,blank=True)
#     email = models.CharField(max_length=100)
#     mobile_number = models.CharField(max_length=12)
#     gender = models.CharField(max_length=1, choices=PERSON_CHOICES, null=True, blank=True)
#     address1 = models.CharField(max_length=30,null=True,blank=True)
#     address2 = models.CharField(max_length=30, null=True, blank=True)
#     apt_number = models.CharField(max_length=20,null=True,blank=True)
#     city = models.CharField(max_length=30,null=True,blank=True)
#     state = models.CharField(max_length=2,choices=US_STATES,null=True,blank=True)
#     zip_code = models.CharField(max_length=5,null=True,blank=True)
#     password = models.CharField(max_length=16,null=True,blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return str(self.patient_id)

class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(HospitalActor,on_delete=models.CASCADE,related_name='doctor',null=True,blank=True)
    patient = models.ForeignKey(HospitalActor,on_delete=models.CASCADE,related_name='patient')
    category = models.CharField(max_length=3, choices=DOCTOR_CATEGORIES, null=True)
    notes = models.CharField(max_length=264,null=True,blank=True)
    treatment_date = models.DateTimeField(null=True,blank=True)
    treatment_notes = models.CharField(max_length=264,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.treatment_id)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(HospitalActor, on_delete=models.CASCADE,related_name='app_doctor')
    patient = models.ForeignKey(HospitalActor, on_delete=models.CASCADE,related_name='app_patient',null=True,blank=True)
    category = models.CharField(max_length=3, choices=DOCTOR_CATEGORIES, null=True)
    booking_date = models.DateField(null=True,blank=True)
    booking_time = models.TimeField(null=True,blank=True)
    is_appointment_confirmed= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.appointment_id)

ORGAN_TYPES = (
    ('HE','Heart'),
    ('IN','Intestines'),
    ('KI','Kidneys'),
    ('LI','Liver'),('LU','Lungs'),('PA','Pancreas')
)

class OrganDonation(models.Model):
    organ_donation_id = models.AutoField(primary_key=True)
    #patient = models.ForeignKey(HospitalActor, on_delete=models.CASCADE
    last_name = models.CharField(max_length=60, null=True, blank=True)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=PERSON_CHOICES, null=True, blank=True)
    address1 = models.CharField(max_length=30, null=True, blank=True)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    apt_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, choices=US_STATES, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    #category = models.CharField(max_length=3, choices=DOCTOR_CATEGORIES, null=True)
    is_organ_donated = models.BooleanField(default=False)
    organ_type = models.CharField(choices=ORGAN_TYPES,max_length=2,null=True,blank=True)
    notes = models.CharField(max_length=264,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.organ_donation_id)


