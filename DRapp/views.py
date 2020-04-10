from django.http import *
from django.shortcuts import render
from DRapp.forms import *
from .models import *
import random


def home(request):
    return render(request, "home.html")


def add(request):
    form1 = PersonalDetails()
    return render(request, "add_patient.html", {'form1': form1})


def pending(request):
    drlist = DiabeticRetinopathy.objects.values_list('patient_id_id', flat=True)
    main_list = list(Patient.objects.exclude(patient_id__in=drlist))
    return render(request, "pending.html", {'pending_list': main_list})


def dr(request, id):

    if request.POST.get('retina_photo_path'):
        category = random.choice(['1','2','3','4','5'])
        confirmation = random.choice(['90','94','95'])
        checking = DiabeticRetinopathy.objects.filter(patient_id_id=id).count()
        if checking == 0:
            diabeticret = DiabeticRetinopathy(patient_id_id=id, retina_photo_path=request.POST.get('retina_photo_path'), predicted_stage=category, confirmation=confirmation)
            diabeticret.save()
        details = DiabeticRetinopathy.objects.filter(patient_id_id=id)
        return render(request, "diabetic_retinopathy.html", {'result': details, 'predicted': True})
    else:
        drform = DiabeticRetinopathyDetails()
        return render(request, "diabetic_retinopathy.html", {'id': id, 'form': drform, 'predicted': False})



def insert(request):
    phone_check = Patient.objects.filter(phone_no=request.POST.get('pno')).count()
    if phone_check == 0:
        new_pid = Patient.objects.all().count() + 1
        patient = Patient(
            patient_id=new_pid,
            patient_name=request.POST.get('pname'),
            patient_age=request.POST.get('page'),
            address=request.POST.get('address'),
            phone_no=request.POST.get('pno'),
            gender=request.POST.get('gender'),
            blood_group=request.POST.get('blood'),
            patient_photo_file_path=request.POST.get('photo_file_path'),
        )
        patient.save()
        diabetic_history = DiabeticHistory(
            patient_id_id=new_pid,
            diabetic_type=request.POST.get('diabetic_type'),
            sugar_Fasting_value=request.POST.get('sugar_Fasting_value'),
            sugar_Non_fasting_value=request.POST.get('sugar_Non_fasting_value'),
            time_duration=request.POST.get('time_duration'),
            diab_report_path=request.POST.get('diab_report_path'),
        )
        diabetic_history.save()
        return HttpResponse("INSERTION SUCCESS")
    else:
        return HttpResponse("Entries already Present")


def get_all(request):
    all = list(Patient.objects.all())
    for i in all:
        if DiabeticRetinopathy.objects.filter(patient_id=i.patient_id).count() != 1:
            all.remove(i)
    return render(request, "listall.html", {'all': all})


def search(request):
    if request.POST.get('pid'):
        parameter = request.POST.get('pid')
        res1 = Patient.objects.filter(patient_id=parameter)
    else:
        parameter = request.POST.get('phno')
        res1 = Patient.objects.filter(phone_no=parameter)
    if res1.count() == 1:
        res2 = DiabeticHistory.objects.filter(patient_id=list(res1)[0].patient_id)
        status = False
        res3 = DiabeticRetinopathy.objects.filter(patient_id=list(res1)[0].patient_id)
        if res3.count() == 1:
            status = True
        return render(request, "patient_personal_details.html", {'ppd': res1, 'pdh': res2, 'dr': res3, 'status': status})
    else:
        return HttpResponse("Patient Not Found")
