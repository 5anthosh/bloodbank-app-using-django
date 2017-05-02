from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from login.models import DonarDetail, BloodStorage


@login_required(login_url='/register/login/')
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm
    return render(request, 'users/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/staff/')
            else:
                return HttpResponse('inactive')
        else:
            return HttpResponse('invalid')
    else:
        return render(request, 'users/login.html')


@login_required(login_url='/register/login/')
def home(request):
    return render(request, 'users/home.html')


@login_required(login_url='/register/login/')
def user_logout(request):
    logout(request)
    return render(request, 'users/login.html')


def public_home(request):
    return render(request, 'users/base2.html',)



def search(request):
    return render(request, 'home/search.html')
def details(request):
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
    return render(request, 'home/details.html', {'list': list2, 'number': number})
def storage(request):
    detail1 = BloodStorage.objects.all()
    return render(request, 'home/blood storage.html', {'detail': detail1})