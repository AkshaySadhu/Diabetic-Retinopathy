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
    patient_photo = models.ImageField(upload_to='patient_photos/', default=None)


class DiabeticHistory(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('TYPE1', 'TYPE1'),
        ('TYPE2', 'TYPE2'),
    )
    diabetic_type = models.CharField(choices=TYPE_CHOICES, max_length=6)
    sugar_Fasting_value = models.IntegerField()
    sugar_Non_fasting_value = models.IntegerField()
    time_duration = models.IntegerField()
    diab_report = models.FileField(upload_to='patient_diabetic_history/', default=None)


class DiabeticRetinopathy(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    retina_photo = models.ImageField(upload_to='patient_retina_photos/', default=None)
    predicted_stage = models.CharField(max_length=10)
    confirmation = models.CharField(max_length=5)

