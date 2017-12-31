from django.shortcuts import render
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MyUserChangeForm
from base_app.views import today_date_weekday,month_installation_count
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_app:login'))


@login_required(login_url='users_app:login')
def user_data(request):
    user_id = request.user.pk
    user = User.objects.get(id=user_id)
    if request.method != 'POST':
        user_change_form = MyUserChangeForm(instance=user)
    else:
        user_change_form = MyUserChangeForm(instance=user, data=request.POST)
        if user_change_form.is_valid():
            user_change_form.save()
    context = {'user_change_form':user_change_form}
    context.update(today_date_weekday())
    context.update(month_installation_count())
    return render(request, 'users_app/user_data.html', context)