from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import DonarDetail, Record, BloodStorage
from .forms import DonateForm
import datetime


@login_required(login_url='/register/login/')
def add_donar(request):
    error = []
    if request.method == 'POST':
        list1 = DonarDetail()
        list1.first_name = str(request.POST['first_name']).capitalize()
        list1.last_name = str(request.POST['last_name']).capitalize()
        list1.name = str(request.POST['first_name']).capitalize() + " " + str(request.POST['last_name']).capitalize()
        print(DonarDetail.objects.all().filter(id_no=request.POST['id_no']))
        if DonarDetail.objects.all().filter(id_no=request.POST['id_no']):
            print(DonarDetail.objects.all().filter(id_no=request.POST['id_no']))
            error.append('ID number already available')
        else:
            list1.id_no = str(request.POST['id_no']).upper()
        list1.gender = request.POST['gender']
        list1.age = request.POST['age']
        list1.blood_group = request.POST['blood_group']
        list1.email = request.POST['email']
        list1.street = request.POST['street']
        list1.street1 = request.POST['street1']
        list1.street2 = request.POST['street2']
        list1.city = str(request.POST['city']).capitalize()
        list1.registered_by = request.user.username
        list1.contact_number = request.POST['contact_number']
        list1.last_donated_date = request.POST['last_donated_date']
        if len(str(list1.last_donated_date)) > 4:
            y, m, d = str(list1.last_donated_date).split('-')
            k = datetime.datetime(int(y), int(m), int(d))
            if k > datetime.datetime.now():
                error.append('provide correct date')
        if len(error) == 0:
            list1.refresh()
            list1.save()
            return HttpResponse('meow')
        else:
            return render(request, 'login/donnarform.html', {'errors': error})
    else:
        return render(request, 'login/donnarform.html', {'errors': error})


def search(request):
    error = 0
    return render(request, 'login/check.html', {'error': error})


def detail(request):
    blood_type = request.POST['blood_group']
    city = str(request.POST['city']).capitalize()
    for i in DonarDetail.objects.all():
        i.refresh()
        i.save()
    list2 = DonarDetail.objects.all().filter(
        blood_group=blood_type,
        city=city,
        number_month=-1,
        ) | DonarDetail.objects.all().filter(
        blood_group=blood_type,
        city=city,
        number_month__gt=2,
        )
    number = len(list2)
    print(number)
    if number > 0:
        return render(request, 'login/details.html', {'list': list2, 'number': number})
    else:
        error = 1
        return render(request, 'login/check.html', {'error': error})


@login_required(login_url='/register/login/')
def donate(request):
    error = []
    if request.method == 'POST':
        record = Record()
        record.blood_TYPE = request.POST['blood_group']
        record.staff = request.user.username
        record.donar_name = str(request.POST['donar_name']).title()
        record.id_no = str(request.POST['id_no']).upper()
        if DonarDetail.objects.all().filter(id_no=str(request.POST['id_no']).upper()):
            if DonarDetail.objects.all().filter(
                    id_no=str(request.POST['id_no']).upper(),
                    blood_group=record.blood_TYPE,
            ):
                if DonarDetail.objects.all().filter(
                        id_no=str(request.POST['id_no']).upper(),
                        blood_group=record.blood_TYPE,
                        number_month__gt=2,
                        ) | DonarDetail.objects.all().filter(
                        id_no=str(request.POST['id_no']).upper(),
                        blood_group=record.blood_TYPE,
                        number_month=-1,
                        ):
                    print('ok')
                else:
                    error.append('donar not eligible')
            else:
                error.append('blood does not match donnar ')
        else:
            error.append('donar not available ')
        if len(error) == 0:
            record.units = request.POST['units']
            record.date = request.POST['date']
            record.save()
        else:
            form = DonateForm()
            return render(request, 'login/donate.html', {'form': form, 'errors': error})
        a = DonarDetail.objects.get(id_no=str(request.POST['id_no']).upper())
        a.last_donated_date = request.POST['date']
        a.refresh()
        a.save()
        storage = BloodStorage()
        if BloodStorage.objects.all().filter(blood_group=request.POST['blood_group']):
            storage1 = BloodStorage.objects.get(blood_group=request.POST['blood_group'])
            storage1.units += float(request.POST['units'])
            storage1.save()
        else:
            storage.blood_group = request.POST['blood_group']
            storage.units = request.POST['units']
            storage.save()
        return HttpResponse('stored')
    else:
        error = []
        form = DonateForm()
        return render(request, 'login/donate.html', {'form': form, 'error': error})


def blood_storage(request):
    detail1 = BloodStorage.objects.all()
    return render(request, 'login/blood.html', {'detail': detail1})


@login_required(login_url='/register/login/')
def records(request):
    detail2 = Record.objects.all()
    return render(request, 'login/records.html', {'detail': detail2})
