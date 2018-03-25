from django.shortcuts import render
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MyUserChangeForm, MyUserCreateForm
#from django.contrib.auth.forms import UserCreationForm
from base_app.views import today_date_weekday,month_installation_count
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_app:login'))


@login_required(login_url='users_app:login')
def user_data(request, user_id=None):
    if request.user.is_staff and user_id!=None:
        user_id = user_id
        other_user_change = user_id
        print (request.user.is_staff, user_id)

    else:
        user_id = request.user.pk
        other_user_change = False
    user = User.objects.get(id=user_id)
    if request.method != 'POST':
        user_change_form = MyUserChangeForm(instance=user)
    else:
        #print(request.POST)
        user_change_form = MyUserChangeForm(instance=user, data=request.POST)
        if user_change_form.is_valid():
            print ('is_valid')
            try:
                print ('is_active')
                if 'is_active' in request.POST:
                    user_change_form.save()
                else:
                    user_change_form.save()
            except:
                print ('except')
                entry = user_change_form.save(commit=False)
                entry.is_active = True
                user_change_form.save()
        else: print (request.POST)
    context = {'user_change_form':user_change_form, 'other_user_change':other_user_change}
    context.update(today_date_weekday())
    context.update(month_installation_count())
    return render(request, 'users_app/user_data.html', context)


@login_required(login_url='users_app:login')
def add_user(request):
    print(request.POST)
    #if request.user.is_staff:
    if request.method != 'POST':
        create_user_form = MyUserCreateForm()
    else:
        create_user_form = MyUserCreateForm(data=request.POST)
        if create_user_form.is_valid():
            new_user = create_user_form.save(commit=False)
            new_user.is_active = True
            new_user.save()
            return HttpResponseRedirect(reverse('users_app:users_list'))
    context = {'create_user_form':create_user_form}
    return render(request, 'users_app/add_user.html', context)

@login_required(login_url='users_app:login')
def users_list(request):
    active_user = User.objects.filter(is_active=True)
    un_active_user = User.objects.filter(is_active=False)
    context = {'active_user':active_user, 'un_active_user':un_active_user}
    return render(request, 'users_app/users_list.html', context)