from django.contrib import admin
from django.urls import path
from app.views import AddTreatmentForPatient, DoctorAppointments, TreatmentHistory, PatientAppointments, \
    DoctorRegistration, PatientHome,DoctorLogin, PatientRegistration, \
    PatientLogin, OrganDonationView, GetAvailableOrgans, DoctorSearch, ShowDoctorAppointments, BookDoctorAppointment,DoctorHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',project2_home,name='project2'),
    path('doctor/signup/', DoctorRegistration, name='doctor_signup'),
    path('doctor/login/', DoctorLogin, name='doctor_login'),
    path('patient/signup/', PatientRegistration, name='patient_signup'),
    path('patient/login/', PatientLogin, name='patient_login'),
    path('organ/donation/', OrganDonationView, name='organ_donation'),
    path('available/organs/', GetAvailableOrgans, name='avl_organs'),
    path('patient/treatment/history/', TreatmentHistory, name='treatment_history'),
    path('patient/treatment/history/<int:patient_id>/', TreatmentHistory, name='treatment_history'),
    path('patient/appointments/', PatientAppointments, name='patient_appointment'),
    path('doctor/appointments/', DoctorAppointments, name='doctor_appointment'),
    path('search/doctors/', DoctorSearch, name='search_doctors'),
    path('show/appointment/<int:doctor_id>/', ShowDoctorAppointments, name='show_appointments'),
    path('book/appointment/<int:doctor_id>/<int:apt_id>/', BookDoctorAppointment, name='book_appointment'),
    path('add/treatment/<int:doctor_id>/<int:patient_id>/', AddTreatmentForPatient, name='add_treatment'),
    path('doctor/home/',DoctorHome,name='doctor_home'),
    path('patient/home/',PatientHome,name='patient_home'),
]
