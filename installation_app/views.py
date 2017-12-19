from django.shortcuts import render
from .forms import InstallationFormAdmin, InstallationFormUser
from django.contrib.auth.models import User
from .models import Installation
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import calendar
import datetime
from base_app.views import today_date_weekday

# Create your views here.
def all_installation(request, day=datetime.date.today().day, month=datetime.date.today().month,
                     year = datetime.date.today().year):
    print(request.COOKIES)
    days_name = {6:'Niedziela', 0:'Poniedziałek', 1:'Wtorek', 2:'środa', 3:'Czwartek', 4:'Piątek', 5:'Sobota'}

    day_in_month = calendar.mdays[month]
    days_list = [datetime.date(year, month, tmp_day).strftime('%d.%m.%Y') for tmp_day in range(1, day_in_month+1)]
    user_id = request.user.pk
    user = User.objects.get(id=user_id)

    if not user.is_staff:
        installations = Installation.objects.filter(Q(employee_1=user_id)| Q(employee_2=user_id)| Q(employee_3=user_id))\
            .filter(date=datetime.date(year, month, day))
    else:
        installations = Installation.objects.filter(date=datetime.date(year, month, day))
    context = {'installations':installations, 'days_list':days_list
               }
    context.update(today_date_weekday())
    print(context)
    return render(request, 'installation_app/all_installation.html', context)


def installation_detail(request, installation_id):
    user_id = request.user.pk
    user = User.objects.get(id=user_id)
    if installation_id == 0:
        installation = None
        initial_data = {'employee_1':user_id, 'date':(datetime.date.today().strftime('%d.%m.%Y'))}
    else:
        installation = Installation.objects.get(id=installation_id)
        initial_data = None

    def get_installation_form(instance=None, data = None, initial=None):
        if not user.is_staff:
            return InstallationFormUser(instance=instance, data=data, initial=initial)
        else:
            return InstallationFormAdmin(instance=instance, data=data, initial=initial)

    if request.method != 'POST':
        installation_form = get_installation_form(instance=installation, initial=initial_data)

    else:
        installation_form = get_installation_form(instance=installation,data=request.POST)
        if installation_form.is_valid():
            new_installation = installation_form.save()
            installation_id = new_installation.id
            if 'submit_and_return' in request.POST:
                installation_date = new_installation.date
                print(installation_date)
                return HttpResponseRedirect(reverse('installation_app:all_installation',
                                                    args=[installation_date.day, installation_date.month,
                                                          installation_date.year]))
            return HttpResponseRedirect(reverse('installation_app:installation_detail', args=[installation_id]))
    context = {'installation_id':installation_id,'installation_form':installation_form}
    return render(request, 'installation_app/installation_detail.html', context)