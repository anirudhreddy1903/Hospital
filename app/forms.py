from django import forms
from .models import PERSON_CHOICES,DOCTOR_CATEGORIES,HospitalActor,US_STATES,ORGAN_TYPES

class DoctorRegistrationForm(forms.Form):
    last_name = forms.CharField(required=True,max_length=60)
    first_name = forms.CharField(required=True,max_length=60)
    category = forms.ChoiceField(required=True,choices=DOCTOR_CATEGORIES)
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(required=True,max_length=10)
    password = forms.CharField(required=True,widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(DoctorRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'


class DoctorLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput())

    def __init__(self,*args,**kwargs):
        super(DoctorLoginForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'


class PatientRegistrationForm(forms.Form):
    last_name = forms.CharField(required=True,max_length=60)
    first_name = forms.CharField(required=True,max_length=60)
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(required=True,max_length=10)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    def __init__(self,*args,**kwargs):
        super(PatientRegistrationForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'

class PatientLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput())

    def __init__(self,*args,**kwargs):
        super(PatientLoginForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'


class AdditionalDetailsForm(forms.ModelForm):
    gender = forms.ChoiceField(required=True,label="Gender",choices=PERSON_CHOICES)
    address1 = forms.CharField(required=True,max_length=30,label="Address1")
    address2 = forms.CharField(required=True, max_length=30, label="Address2")
    apt_number = forms.CharField(required=True, max_length=10, label="Apt #")
    city = forms.CharField(required=True, max_length=50, label="City")
    state = forms.ChoiceField(required=True,choices=US_STATES, label="State")
    zip_code = forms.CharField(required=True,label="Zip Code",max_length=5)

    def __init__(self,*args,**kwargs):
        super(AdditionalDetailsForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'

    class Meta:
        model = HospitalActor
        fields = ("gender","address1","address2","apt_number","city","state","zip_code")


class OrganDonationForm(forms.Form):
    last_name = forms.CharField(required=True, max_length=60)
    first_name = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(required=True)
    gender = forms.ChoiceField(required=True, label="Gender",choices=PERSON_CHOICES)
    address1 = forms.CharField(required=True, max_length=30, label="Address1")
    address2 = forms.CharField(required=True, max_length=30, label="Address2")
    apt_number = forms.CharField(required=True, max_length=10, label="Apt #")
    city = forms.CharField(required=True, max_length=50, label="City")
    state = forms.ChoiceField(required=True, choices=US_STATES, label="State")
    zip_code = forms.CharField(required=True, label="Zip Code", max_length=5)
    organ_type = forms.ChoiceField(choices=ORGAN_TYPES,required=True)
    notes = forms.CharField(required=True,max_length=264, label="Danor Notes")

    def __init__(self,*args,**kwargs):
        super(OrganDonationForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'


class DoctorSearchForm(forms.Form):
    search_str = forms.CharField(max_length=60,required=True,label="Search using last name")
    def __init__(self,*args,**kwargs):
        super(DoctorSearchForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-solid'


class AddTreatmentForm(forms.Form):
    notes = forms.CharField(max_length=264, required=True, label="Treatment Notes",
                            widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}))
