import datetime
from .forms import AdditionalDetailsForm, OrganDonationForm, PatientLoginForm, PatientRegistrationForm, DoctorLoginForm, \
    DoctorRegistrationForm, DoctorSearchForm, AddTreatmentForm

from .models import HospitalActor, OrganDonation, Treatment, Appointment
from django.shortcuts import render, redirect, reverse

from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def project2_home(request):
    return render(request,'project2_home.html')

def DoctorRegistration(request):
    http_method = request.method
    msg = ''
    if http_method == "POST":
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            category = form.cleaned_data["category"]
            first_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            mobile_number = form.cleaned_data["mobile_number"]
            password = form.cleaned_data["password"]
            if HospitalActor.objects.filter(email=email).exists():
                msg = "Email address is already exists."
            user = HospitalActor.objects.create(last_name=last_name, first_name=first_name, category=category)
            user.set_password = password
            user.mobile_number = mobile_number
            user.save()
            print(" user created successfully")
            return redirect('doctor_home')
    else:
        msg = ''
        form = DoctorRegistrationForm()
    return render(request, 'doctor_signup.html', {'form': form, 'msg': msg})


def DoctorLogin(request):
    if request.user.is_active:
        return redirect('doctor_home')
    error_msg = ''
    if request.method == "POST":
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if HospitalActor.objects.filter(email=email).exists():
                error_msg = 'Doctor is not exists with email ' + str(email)
            user = HospitalActor.objects.filter(email=email).first()
            if not user.check_password(password):
                error_msg = "Password is incorrect."
            return redirect('doctor_home')
    else:
        form = DoctorLoginForm()
        return render(request, 'doctor_login.html', {'form': form, 'error_msg': error_msg})

def DoctorHome(request):
    if not request.user.is_active:
        return redirect('doctor_login')
    return render(request,'doctor_home.html')

def PatientHome(request):
    if not request.user.is_active:
        return redirect('patient_login')
    return render(request,'patient_home.html')

def PatientRegistration(request):
    http_method = request.method
    msg = ''
    if http_method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            category = form.cleaned_data["category"]
            first_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            mobile_number = form.cleaned_data["mobile_number"]
            password = form.cleaned_data["password"]
            if HospitalActor.objects.filter(email=email).exists():
                msg = "Email address is already exists."
            user = HospitalActor.objects.create(last_name=last_name, first_name=first_name, category=category)
            user.set_password = password
            user.mobile_number = mobile_number
            user.save()
            print(" user created successfully")
            return redirect('doctor_home')
    else:
        msg = ''
        form = PatientRegistrationForm()
    return render(request, 'patient_signup.html', {'form': form, 'msg': msg})


def PatientLogin(request):
    if request.user.is_active:
        return redirect('doctor_home')
    error_msg = ''
    if request.method == "POST":
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if HospitalActor.objects.filter(email=email).exists():
                error_msg = 'Doctor is not exists with email ' + str(email)
            user = HospitalActor.objects.filter(email=email).first()
            if not user.check_password(password):
                error_msg = "Password is incorrect."
            return redirect('patient_home')
    else:
        form = DoctorLoginForm()
        return render(request, 'patient_login.html', {'form': form, 'error_msg': error_msg})


class UserMiniAddressViewJUX(LoginRequiredMixin, UpdateView):
    model = HospitalActor
    form_class = AdditionalDetailsForm
    template_name = 'additional_details.html'

    def get_success_url(self):
        return reverse('complete_profile')

    def get_object(self):
        return HospitalActor.objects.get(username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super(UserMiniAddressViewJUX, self).get_context_data(**kwargs)
        return context


def TreatmentHistory(request, patient_id=None):
    if not request.user.is_active:
        return redirect('patient_login')
    if patient_id:
        patient = HospitalActor.objects.filter(pk=patient_id).first()
    else:
        patient = request.user
    treatments = Treatment.objects.filter(patient=patient)
    return render(request, 'treatment_history.html', {'treatments': treatments, 'patient': patient})


def AddTreatmentForPatient(request, doctor_id, patient_id):
    if not request.user.is_active:
        return redirect('doctor_login')
    doctor = HospitalActor.objects.filter(pk=doctor_id).first()
    if not doctor:
        return redirect('search_doctors')
    patient = HospitalActor.objects.filter(pk=patient_id).first()
    if not patient:
        return redirect('search_doctors')
    if request.method == "POST":
        form = AddTreatmentForm(request.POST)
        if form.is_valid():
            treatment_notes = form.cleaned_data["notes"]
            treatment = Treatment.objects.create(doctor=doctor, patient=patient, treatment_notes=treatment_notes)
            treatment.treatment_date = datetime.datetime.now()
            treatment.save()
            # messages.add_message(request,messages.SUCCESS,'Treatment notes updated successfully for patient ' + str(patient.first_name))
            return redirect('doctor_appointment')
    else:
        form = AddTreatmentForm()

    return render(request, 'add_treatment.html', {'doctor': doctor, 'patient': patient, 'form': form})


def DoctorAppointments(request):
    if not request.user.is_active:
        return redirect('doctor_login')
    doctor = request.user
    appointments = Appointment.objects.filter(doctor=doctor, is_appointment_confirmed=True)
    return render(request, 'doctor_appointment_history.html', {'appointments': appointments})


def PatientAppointments(request):
    if not request.user.is_active:
        return redirect('patient_login')
    patient = request.user
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'appointment_history.html', {'appointments': appointments})


def DoctorSearch(request):
    doctors = []
    if request.method == "POST":
        form = DoctorSearchForm(request.POST)
        if form.is_valid():
            search_str = form.cleaned_data["search_str"]
            doctors = HospitalActor.objects.only("last_name", "first_name", "category", "pk").filter(is_patient=False,
                                                                                                     last_name__icontains=search_str)


    else:
        form = DoctorSearchForm()
    return render(request, 'search_doctor.html', {'doctors': doctors, 'form': form})


def ShowDoctorAppointments(request, doctor_id):
    if not request.user.is_active:
        return redirect('patient_login')
    doctor = HospitalActor.objects.filter(pk=doctor_id).first()
    if not doctor:
        return redirect('search_doctors')
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'book_appointment.html', {'doctor': doctor, 'appointments': appointments})


def BookDoctorAppointment(request, doctor_id, apt_id):
    if not request.user.is_active:
        return redirect('patient_login')
    doctor = HospitalActor.objects.filter(pk=doctor_id).first()
    if not doctor:
        # messages.add_message(request,messages.INFO,"No doctor found with " + str(doctor_id))
        return redirect('search_doctors')
    appointment = Appointment.objects.filter(pk=apt_id).first()
    if not appointment:
        # messages.add_message(request, messages.INFO, "No appointment found for the doctor id " + str(doctor_id))
        return redirect('search_doctors')
    appointment.is_appointment_confirmed = True
    appointment.patient = request.user
    appointment.save()
    # messages.add_message(request, messages.SUCCESS, "Appointment booked successfully"
    return redirect('patient_appointment')


def OrganDonationView(request):
    msg = ''
    if request.method == "POST":
        form = OrganDonationForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            first_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            mobile_number = form.cleaned_data["mobile_number"]
            gender = form.cleaned_data["gender"]
            address1 = form.cleaned_data["address1"]
            address2 = form.cleaned_data["address2"]
            apt_number = form.cleaned_data["apt_number"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zip_code = form.cleaned_data["zip_code"]
            organ_type = form.cleaned_data["organ_type"]
            organ, oragn_flag = OrganDonation.objects.get_or_create(email=email, mobile_number=mobile_number,
                                                                    organ_type=organ_type)
            if oragn_flag:
                organ.last_name = last_name
                organ.first_name = first_name
                organ.gender = gender
                organ.address1 = address1
                organ.address2 = address2
                organ.city = city
                organ.state = state
                organ.zip_code = zip_code
                organ.save()
            msg = "Your ogran donation " + str(
                organ_type) + " saved successfully." if oragn_flag else "You already donated the organ " + str(
                organ_type)

    else:
        form = OrganDonationForm()
    return render(request, 'organ_donation.html', {'form': form, 'msg': msg})


def GetAvailableOrgans(request):
    organs = OrganDonation.objects.all()
    return render(request, 'avl_organs.html', {'organs': organs})
