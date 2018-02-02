import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from installation_app.models import Installation
from django.contrib.auth.models import User
from base_app.views import month_name, today_date_weekday, month_installation_count


def get_employee_report(employee, month, year):
    return Installation.objects.filter(date__month=month, date__year=year, accepted=True, success=True). \
        filter(Q(employee_1=employee) |
               Q(employee_2=employee) |
               Q(employee_3=employee))

# Create your views here.
@login_required(login_url='users_app:login')
def month_report(request, month, year, employee = None, detail=True):
    user_id = request.user.pk
    if request.user.is_staff:
        print('is_staff')
        try:
            if not employee:
                report = Installation.objects.filter(date__month=month, date__year=year, accepted=True)
                if detail == True:
                    users_list = {}
                    for user in User.objects.filter(is_staff=False).order_by('first_name'):
                        user_installations = get_employee_report(user.id,month,year)
                        users_list[user.first_name + ' ' + user.last_name] = []
                        users_list[user.first_name+' '+user.last_name].append(len(user_installations))
                        users_list[user.first_name + ' ' + user.last_name].append([0, 0, 0])
                        for installation in user_installations:
                            #print(installation.employee_1, installation.employee_2, installation.employee_3)
                            if (installation.employee_1 == None and installation.employee_2 == None) \
                                or (installation.employee_2 == None and installation.employee_3 == None) \
                                    or (installation.employee_3 == None and installation.employee_1 == None):
                                        users_list[user.first_name + ' ' + user.last_name][1][0]+=1
                            elif (installation.employee_1 == None and (installation.employee_2  != None and installation.employee_3 != None)) \
                                or (installation.employee_2 == None and (installation.employee_3  != None and installation.employee_1 != None)) \
                                    or (installation.employee_3 == None and (installation.employee_1 != None and installation.employee_2 != None)):
                                        users_list[user.first_name + ' ' + user.last_name][1][1]+=1
                            else:
                                users_list[user.first_name + ' ' + user.last_name][1][2] += 1
            else:
                report = get_employee_report(employee, month, year)
        except:
            return HttpResponseRedirect (reverse ('reports_app:list_month_report'))
    else:
        print('user')
        try:
            report = get_employee_report(user_id, month, year)
        except:
            return HttpResponseRedirect (reverse ('reports_app:list_month_report'))
    context = {'report':report, 'month':month, 'year':year, 'employee':employee,
               'len_contract':len(report.filter(with_contract=True))}
    print(type(month))
    try:context.update({'users_installations_list':users_list, 'count_installations':len(report)})
    except:pass
    context.update(today_date_weekday())
    context.update({'dict_month_name': month_name(month)})
    context.update(month_installation_count(user_id=user_id))
    return render(request, 'reports_app/month_report.html', context)


@login_required(login_url='users_app:login')
def list_month_report(request, employee=None):
    if request.user.is_staff and employee:
        employees = User.objects.filter(is_staff=False, is_active=True)
    else:
        employees = employee
    user_id = request.user.pk
    context = {'month_name':month_name(), 'employees':employees, 'year':datetime.date.today().year}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=user_id))
    context.update(month_name())
    context.update({'dict_month_name': month_name()})
    return render(request, 'reports_app/list_month_report.html', context)


@login_required(login_url='users_app:login')
def working_time(request, ts_month=datetime.date.today().month, year=datetime.date.today().year, employee=None):
    day_count = calendar.monthrange(year, ts_month)[1]
    installation_list = get_employee_report(employee, ts_month, year)
    installation_list_to_context = []
    list_working_time = []
    for i in range(1, day_count+1):
        installation_list_to_context.append([])
        list_working_time.append(0)
        for installation in installation_list:
            if installation.date.day == i:
                installation_list_to_context[i-1].append(installation)
                list_working_time[i-1]+=3
    time_result = 0
    inst_result = 0
    zip_lists = zip(installation_list_to_context,list_working_time)
    for inst in installation_list_to_context:
        inst_result += len(inst)

    for time in list_working_time:
        time_result += time

    context = {'day_count':day_count, 'zip_lists':zip_lists,'inst_result':inst_result,'time_result':time_result,
               'ts_month':int(ts_month), 'year':year, 'employee':User.objects.get(id=employee)}
    context.update(today_date_weekday())
    context.update({'dict_month_name': month_name()})
    context.update(month_installation_count(user_id=employee))
    return render(request, 'reports_app/working_time.html', context)


@login_required(login_url='users_app:login')
def create_working_time(request):
    employee = request.user.pk
    employees = User.objects.filter(is_staff=False, is_active=True)
    context = {'employees':employees}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=employee))
    context.update({'dict_month_name': month_name()})
    return render(request, 'reports_app/create_working_time.html', context)


