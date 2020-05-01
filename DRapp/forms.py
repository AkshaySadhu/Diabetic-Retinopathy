from django.forms import *

from DRapp.models import Patient


class PersonalDetails(forms.Form):
    pname = CharField(label='Enter patient\'s name', max_length=30, required=True)
    page = IntegerField(label='Enter patient\'s age', max_value=100, required=True)
    address = CharField(label='Enter patient\'s address', max_length=100, required=True)
    pno = IntegerField(label='Enter patient\'s phone Number', max_value=100000000000, min_value=0, required=True)
    gender = ChoiceField(label='Gender', choices=(('M', 'Male'), ('F', 'Female')))
    blood = ChoiceField(label="Blood Group", choices=(('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')))
    patient_photo = ImageField(label='Enter the file path of photo', required=True)
    diabetic_type = ChoiceField(label='Diabetic Type', choices=(('type1', 'TYPE1'), ('type2', 'TYPE2')), required=True)
    sugar_Fasting_value = IntegerField(label='Sugar Fasting Value', required=True)
    sugar_Non_fasting_value = IntegerField(label='Sugar Non Fasting Value', required=True)
    time_duration = IntegerField(label="Duration of Diabeties", max_value=70, min_value=2, required=True)
    diab_report = FileField(label='Enter file path of Diabetic Report', required=True)


class DiabeticRetinopathyDetails(forms.Form):
    retina_photo = ImageField(label='Retina photo', required=True)
    predicted_stage = CharField(label='Predicted Stage', max_length=10, required=True, disabled=True)
    confirmation = CharField(label='Confirmation Percentage', max_length=5, required=True, disabled=True)
