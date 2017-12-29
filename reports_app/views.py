from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from installation_app.models import Installation
from django.contrib.auth.models import User
from base_app.views import month_name, today_date_weekday, month_installation_count



# Create your views here.

def month_report(request, month, year, employee = None):
    user_id = request.user.pk
    if request.user.is_staff:
        print('is_staff')
        try:
            if not employee:
                report = Installation.objects.filter(date__month=month, date__year=year).order_by('date').order_by('address')
            else:
                report = Installation.objects.filter(date__month=month, date__year=year).filter(Q(employee_1=employee) |
                                                                                                Q(employee_2=employee) |
                                                                                                Q(employee_3=employee))
        except:
            return HttpResponseRedirect (reverse ('reports_app:list_month_report'))
    else:
        print('user')
        try:
            report = Installation.objects.filter(date__month=month, date__year=year).filter(Q(employee_1=user_id)|
                                                                                            Q(employee_2=user_id)|
                                                                                            Q(employee_3=user_id))
        except:
            return HttpResponseRedirect (reverse ('reports_app:list_month_report'))
    context = {'report':report, 'month':month_name(month), 'year':year, 'employee':employee}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=user_id))
    return render(request, 'reports_app/month_report.html', context)


def list_month_report(request, employee=None):
    if request.user.is_staff and employee:
        employees = User.objects.filter(is_staff=False, is_active=True)
    else:
        employees = employee
    user_id = request.user.pk
    context = {'month_name':month_name(), 'employees':employees}
    context.update(today_date_weekday())
    context.update(month_installation_count(user_id=user_id))
    return render(request, 'reports_app/list_month_report.html', context)


