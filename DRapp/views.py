from django.http import *
from django.shortcuts import *
from DRapp.forms import *
from .models import *
import random
from django.contrib.auth import authenticate, login


def prelogin(request):
    return render(request, "login.html")

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

    if request.method == 'POST':
        files = request.FILES
        files['retina_photo'].name = str(id) + '_retina.' + files['retina_photo'].name.split('.')[-1]
        category = random.choice(['1','2','3','4','5'])
        confirmation = random.choice(['90','94','95'])
        checking = DiabeticRetinopathy.objects.filter(patient_id_id=id).count()
        if checking == 0:
            diabeticret = DiabeticRetinopathy(patient_id_id=id, retina_photo=files['retina_photo'], predicted_stage=category, confirmation=confirmation)
            diabeticret.save()
        details = DiabeticRetinopathy.objects.filter(patient_id_id=id)
        return render(request, "diabetic_retinopathy.html", {'result': details, 'predicted': True})
    else:
        drform = DiabeticRetinopathyDetails()
        return render(request, "diabetic_retinopathy.html", {'id': id, 'form': drform, 'predicted': False})



def insert(request):
    data = request.POST
    files = request.FILES
    if request.method == 'POST':
        check = Patient.objects.filter(phone_no=data['pno'], patient_name=data['pname'], patient_age=data['page'], blood_group=data['blood']).count()
        if check == 0:
            new_pid = Patient.objects.order_by('-patient_id').first()
            if new_pid == None:
                new_pid = 1
            else:
                new_pid = new_pid.patient_id + 1
            files['patient_photo'].name = str(new_pid) + '.' + files['patient_photo'].name.split('.')[-1]
            files['diab_report'].name = str(new_pid) + '.' + files['diab_report'].name.split('.')[-1]
            patient = Patient(
                patient_id=new_pid,
                patient_name=data['pname'],
                patient_age=data['page'],
                address=data['address'],
                phone_no=data['pno'],
                gender=data['gender'],
                blood_group=data['blood'],
                patient_photo=files['patient_photo'],
            )
            patient.save()
            diabetic_history = DiabeticHistory(
                patient_id_id=new_pid,
                diabetic_type=data['diabetic_type'],
                sugar_Fasting_value=data['sugar_Fasting_value'],
                sugar_Non_fasting_value=data['sugar_Non_fasting_value'],
                time_duration=data['time_duration'],
                diab_report=files['diab_report'],
            )
            diabetic_history.save()
            return HttpResponse("INSERTION SUCCESS")
        else:
            return HttpResponse("entries already present")
    else:
        return HttpResponse("Entries already Present")


def get_all(request):
    all = list(Patient.objects.all())
    return render(request, "listall.html", {'all': all})


def search(request):
    if request.method == 'POST':
        data = request.POST
        search_key = data['parameter']
        res1 = ''
        if str(search_key).isalpha():
            res1 = Patient.objects.filter(patient_name__icontains=search_key)
        elif str(search_key).isnumeric():
            res1 = Patient.objects.filter(phone_no=int(search_key))
        return render(request, "search_result.html", {'search_result': res1, 'search_key': search_key})
    else:
        return HttpResponse("Something went wrong")


def loggingin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home/')
    else:
        return HttpResponse("Invalid Credentials")
