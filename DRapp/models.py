from django.db import models


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    phone_no = models.BigIntegerField(unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group_choices = (('A+', 'apos'),
                           ('A-', 'aneg'),
                           ('B+', 'bpos'),
                           ('B-', 'bneg'),
                           ('O+', 'opos'),
                           ('O-', 'oneg'),
                           ('AB+', 'abpos'),
                           ('AB-', 'abneg'),
                           )
    blood_group = models.CharField(choices=blood_group_choices, max_length=3)
    patient_photo_file_path = models.CharField(max_length=100)


class DiabeticHistory(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diabetic_type = models.CharField(max_length=6)
    sugar_Fasting_value = models.CharField(max_length=15)
    sugar_Non_fasting_value = models.CharField(max_length=15)
    time_duration = models.IntegerField()
    diab_report_path = models.CharField(max_length=100)


class DiabeticRetinopathy(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    retina_photo_path = models.CharField(max_length=100)
    predicted_stage = models.CharField(max_length=10)
    confirmation = models.CharField(max_length=5)

