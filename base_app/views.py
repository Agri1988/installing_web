import datetime
from django.shortcuts import render
from installation_app.models import Installation

# Create your views here.
def today_date_weekday():
    days_name = {6: 'Niedziela', 0: 'Poniedziałek', 1: 'Wtorek', 2: 'środa', 3: 'Czwartek', 4: 'Piątek', 5: 'Sobota'}
    return {'today_date': datetime.date.today().strftime('%d.%m.%Y'),
               'today_weekday': days_name[datetime.date.today().weekday()]}

def month_installation_count(month=datetime.date.today().month, year=datetime.date.today().year):
    return {'installation_in_month':Installation.objects.filter(date__month=month).filter(date__year=year).filter(success=True)}


def index(request):
    context = today_date_weekday()
    context.update(month_installation_count())
    return render(request, 'base_app/base.html', context)