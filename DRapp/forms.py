from django.forms import *


class PersonalDetails(forms.Form):
    pname = CharField(label='Enter patient\'s name', max_length=30, required=True)
    page = IntegerField(label='Enter patient\'s age', max_value=100, required=True)
    address = CharField(label='Enter patient\'s address', max_length=100, required=True)
    pno = IntegerField(label='Enter patient\'s phone Number', max_value=100000000000, min_value=0, required=True)
    gender = ChoiceField(label='Gender', choices=(('M', 'Male'), ('F', 'Female')))
    blood = ChoiceField(label="Blood Group", choices=(('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')))
    photo_file_path = CharField(label='Enter the file path of photo', required=True)
    diabetic_type = ChoiceField(label='Diabetic Type', choices=(('type1', 'TYPE1'), ('type2', 'TYPE2')), required=True)
    sugar_Fasting_value = CharField(label='Sugar Fasting Value', max_length=15, required=True)
    sugar_Non_fasting_value = CharField(label='Sugar Non Fasting Value', max_length=15, required=True)
    time_duration = IntegerField(label="Duration of Diabeties", max_value=70, min_value=2, required=True)
    diab_report_path = CharField(label='Enter file path of Diabetic Report', max_length=100, required=True)


class DiabeticRetinopathyDetails(forms.Form):
    retina_photo_path = CharField(label='Retina photo path', max_length=100, required=True)
    predicted_stage = CharField(label='Predicted Stage', max_length=10, required=True, disabled=True)
    confirmation = CharField(label='Confirmation Percentage', max_length=5, required=True, disabled=True)
