import datetime
from django.shortcuts import render

# Create your views here.
def today_date_weekday():
    days_name = {6: 'Niedziela', 0: 'Poniedziałek', 1: 'Wtorek', 2: 'środa', 3: 'Czwartek', 4: 'Piątek', 5: 'Sobota'}
    return {'today_date': datetime.date.today().strftime('%d.%m.%Y'),
               'today_weekday': days_name[datetime.date.today().weekday()]}

def index(request):
    context = today_date_weekday()
    return render(request, 'base_app/base.html', context)