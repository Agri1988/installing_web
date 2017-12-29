import datetime

from django.db.models import Q
from django.shortcuts import render
from installation_app.models import Installation

# Create your views here.
def month_name(month_number = None):
    dict_month_name = {1:'Styczen', 2:'Luty', 3:'Marzec', 4:'Kwiecin', 5:'Maj', 6:'Czerwiec', 7:'Lipiec', 8:'Sierpien',
                       9:'wrzesien', 10:'Pazdziernik', 11:'Listopad', 12:'Grudzien'}
    if month_number:
        return dict_month_name[int(month_number)]
    else:
        return dict_month_name


def today_date_weekday():
    days_name = {6: 'Niedziela', 0: 'Poniedziałek', 1: 'Wtorek', 2: 'środa', 3: 'Czwartek', 4: 'Piątek', 5: 'Sobota'}
    return {'today_date': datetime.date.today().strftime('%d.%m.%Y'),
               'today_weekday': days_name[datetime.date.today().weekday()]}

def month_installation_count(month=datetime.date.today().month, year=datetime.date.today().year, user_id=None):
    result = Installation.objects.filter(date__month=month,date__year=year,success=True,
                                                                accepted=True)
    if user_id:
        result = result.filter(Q(employee_1=user_id)| Q(employee_2=user_id)| Q(employee_3=user_id))
    return {'installation_in_month':result}


def index(request):
    context = today_date_weekday()
    context.update(month_installation_count(user_id=request.user.pk))
    return render(request, 'base_app/base.html', context)