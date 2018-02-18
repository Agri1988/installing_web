from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
import calendar
import datetime

from base_app.views import today_date_weekday,month_installation_count
from .models import Installation, InstallationImage
from .forms import InstallationFormAdmin, InstallationFormUser, InstallationStandartForm

def get_today_date():
    day, month, year = datetime.datetime.utcnow().day, datetime.datetime.utcnow().month, datetime.datetime.utcnow().year
    return day, month, year

# Create your views here.
@login_required(login_url='users_app:login')
def all_installation(request, day=None, month=None,year=None):
    if day==None and month==None and year==None:
        day, month, year = get_today_date()
    day_in_month = calendar.mdays[month]
    days_list = [datetime.date(year, month, tmp_day).strftime('%d.%m.%Y') for tmp_day in range(1, day_in_month+1)]
    user_id = request.user.pk
    user = User.objects.get(id=user_id)

    if not user.is_staff:
        installations = Installation.objects.filter(Q(employee_1=user_id)| Q(employee_2=user_id)| Q(employee_3=user_id))\
            .filter(date=datetime.date(year, month, day))
    else:
        installations = Installation.objects.filter(date=datetime.date(year, month, day))
    day = str(day)
    context = {'installations':installations, 'days_list':days_list, 'view_day':('0'+day if len(day)!=2 else day),
               'month':month, 'year':year}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=user_id))
    print(day, month, year)
    return render(request, 'installation_app/all_installation.html', context)


@login_required(login_url='users_app:login')
def installation_detail(request, installation_id, day=datetime.date.today().day, month=datetime.date.today().month,
                     year = datetime.date.today().year):
    user_id = request.user.pk
    user = User.objects.get(id=user_id)
    print(datetime.date(year,month,day).strftime('%d.%m.%Y'))
    installation_images = None
    if installation_id == 0:
        installation = None
        initial_data = {'employee_1':user_id, 'date':(datetime.date(year,month,day).strftime('%d.%m.%Y'))}
    else:
        installation = Installation.objects.get(id=installation_id)
        initial_data = None
        installation_images = InstallationImage.objects.filter(installation=installation_id)

    def get_installation_form(instance=None, data = None, initial=None):
        if not user.is_staff:
            return InstallationFormUser(instance=instance, data=data, initial=initial)
        else:
            return InstallationFormAdmin(instance=instance, data=data, initial=initial)

    if request.method != 'POST':
        installation_form = get_installation_form(instance=installation, initial=initial_data)
        try:
            if not user.is_staff and installation.accepted != False:
                return HttpResponseRedirect(reverse('installation_app:all_installation',
                                                    args=[installation.date.day, installation.date.month,
                                                          installation.date.year]))
        except AttributeError:pass
    else:
        installation_form = get_installation_form(data=request.POST, instance=installation)
        if installation_form.is_valid():
            new_installation = installation_form.save()
            installation_id = new_installation.id
            if request.FILES:
                new_installation_image = InstallationImage()
                new_installation_image.installation_id=installation_id
                new_installation_image.image = request.FILES['image']
                new_installation_image.save()
            if 'submit_and_return' in request.POST:
                installation_date = new_installation.date
                print(installation_date)
                return HttpResponseRedirect(reverse('installation_app:all_installation',
                                                    args=[installation_date.day, installation_date.month,
                                                          installation_date.year]))
            return HttpResponseRedirect(reverse('installation_app:installation_detail', args=[installation_id]))
    context = {'installation_id':installation_id,'installation_form':installation_form, 'installation':installation,
               'installation_images':installation_images}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=user_id))
    context.update()
    return render(request, 'installation_app/installation_detail.html', context)


@login_required(login_url='users_app:login')
def delete_installation(request, installation_id, day, month, year):
    print(installation_id)
    if request.user.is_staff:
        installation_images = InstallationImage.objects.filter(installation=installation_id)
        print(installation_images)
        for installation_image in installation_images:
            installation_image.delete()
        installation = Installation.objects.get(id=installation_id)
        installation.delete()

    return HttpResponseRedirect(reverse('installation_app:all_installation',args=[day, month,year]))


@login_required(login_url='users_app:login')
def delete_installation_image(request, installation_image_id):
    installation_image = InstallationImage.objects.get(id=installation_image_id)
    installation_id = installation_image.installation.id
    installation_image.delete()
    return HttpResponseRedirect(reverse('installation_app:installation_detail',args=[installation_id]))

def add_field_element(request, template, form, fieldname):
    if request.user.is_staff:
        print(request.GET)
        if request.method != 'POST':
            print('get')
            context = {'form': form()}
            template = get_template(template)
            return HttpResponse(template.render(context, request))
        else:
            print(request.POST)
            form = form(data=request.POST)
            if form.is_valid():
                print('valid')
                new_element = form.save()
                new_element_id = new_element.id
                new_element_name = getattr(new_element, fieldname)
                print(new_element_name)
            data_dict = {'new_element_id':new_element_id, 'new_element_name':new_element_name}
            return JsonResponse(data_dict)


def add_image(request, installation_id):
    pass
