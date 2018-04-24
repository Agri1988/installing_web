import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse

from installation_app.models import Installation
from .models import Car, MileageAccount, CarRefueling
from .forms import CarForm, MileageAccountWithInstallationForm, MileageAccountWithOutInstallationForm, CarRefuelingForm

# Create your views here.
@login_required(login_url='users_app:login')
def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'mileage_account_app/all_cars.html', {'cars':cars})


@login_required(login_url='users_app:login')
def detail_car(request, car_id=None):
    if request.user.is_staff:
        if car_id != None:
            car = Car.objects.get(id=car_id)
        else:
            car = car_id
        if request.method != 'POST':
            form = CarForm(instance=car)
        else:
            form = CarForm(instance=car, data=request.POST)
            if form.is_valid():
                new_car = form.save()
                car_id = new_car.id
                return HttpResponseRedirect(reverse('mileage_account_app:all_cars'))
        context = {'car':car, 'form':form}
        return render(request, 'mileage_account_app/new_car.html', context)
    else:
        return HttpResponseRedirect(reverse('mileage_account_app:all_cars'))


@login_required(login_url='users_app:login')
def all_mileage_accounts(request):
    cars = Car.objects.all()
    mileage_accounts = MileageAccount.objects.filter(car=cars[0].id)
    context = {'mileage_accounts':(mileage_accounts[len(mileage_accounts)-31:] if len(mileage_accounts)>31
    else mileage_accounts), 'cars':cars, 'selected_car':cars[0].id}
    return render(request, 'mileage_account_app/all_mileage_accounts.html', context)


def car_mileage_accounts(request, car_id):
    mileage_accounts = MileageAccount.objects.filter(car=car_id)
    print(len(mileage_accounts))
    cars = Car.objects.all()
    context = {'mileage_accounts':mileage_accounts , 'cars':cars, 'selected_car':car_id}
    return render(request, 'mileage_account_app/all_mileage_accounts.html', context)


@login_required(login_url='users_app:login')
def detail_mileage_account(request, mileage_account_id=None):
    print(request.method)
    def get_form(instance, initial=None, installation=True, data=None):
        if installation:
            return MileageAccountWithInstallationForm(instance=instance, initial=initial, data=data)
        else:
            return MileageAccountWithOutInstallationForm(instance=instance, initial=initial, data=data)
    if mileage_account_id != None:
        mileage_account = MileageAccount.objects.get(id=mileage_account_id)
    else:
        mileage_account = mileage_account_id
    if request.method != 'POST':
        if mileage_account != None:
            if mileage_account.installation != None:
                form = get_form(instance=mileage_account, installation=True,
                                initial={'date':mileage_account.date.strftime('%Y-%m-%d')})
            else:
                form = get_form(instance=mileage_account, installation=False)
        else:
            form = get_form(instance=mileage_account, initial={'date':datetime.date.today().strftime('%Y-%m-%d')},
                            installation=False)
    else:
        form = get_form(instance=mileage_account, data=request.POST)
        if form.is_valid():
            new_mileage_account = form.save(commit=False)
            if request.POST.get('comments'):
                new_mileage_account.comments = request.POST['comments']
            elif request.POST.get('installation'):
                new_mileage_account.installation = Installation.objects.get(id=request.POST['installation'])
            new_mileage_account.save()
            return HttpResponseRedirect(reverse('mileage_account_app:all_mileage_accounts'))
    context = {'mileage_account':mileage_account, 'form':form}
    return render(request, 'mileage_account_app/new_mileage_account.html', context)


@login_required(login_url='users_app:login')
def detail_mileage_account_base_installation(request, installation_id, date, user):
    form = MileageAccountWithInstallationForm(instance=MileageAccount(),
            initial={'installation':Installation.objects.get(id=installation_id),
                     'date':date, 'user': User.objects.get(id=user)})
    print(installation_id, date, user)
    context = {'form':form, 'installation_id':installation_id}
    template = get_template('mileage_account_app/base_new_mileage_account.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='users_app:login')
def get_last_mileage(request, car_id):
    mileage_accounts = MileageAccount.objects.filter(car=car_id).order_by('-end_mileage')
    for i in mileage_accounts:
        print(i.end_mileage)
    end_mileage = mileage_accounts[0].end_mileage if len(mileage_accounts)>0 else 0
    return JsonResponse({'last_mileage':end_mileage})


@login_required(login_url='users_app:login')
def all_car_refueling(request, car_id=None):
    cars = Car.objects.all()
    if car_id == None:
        car_refuelings = CarRefueling.objects.filter(car=cars[0].id)
    else:
        car_refuelings = CarRefueling.objects.filter(car=car_id)
    context = {'car_refuelings':car_refuelings, 'cars':cars, 'selected_car':car_id if car_id != None else cars[0].id}
    return render(request, 'mileage_account_app/all_car_refueling.html', context)


@login_required(login_url='users_app:login')
def detail_car_refueling(request, car_refueling_id=None):
    if car_refueling_id != None:
        car_refueling = CarRefueling.objects.get(id=car_refueling_id)
    else:
        car_refueling = None

    if request.method != 'POST':
        form = CarRefuelingForm(instance=car_refueling)
    else:
        form = CarRefuelingForm(instance=car_refueling, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mileage_account_app:all_car_refueling'))
    context = {'car_refueling': car_refueling, 'form': form}
    return render(request, 'mileage_account_app/new_car_refueling.html', context)



