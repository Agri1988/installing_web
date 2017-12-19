from django.urls import path, include
from django.contrib.auth.views import login, password_change
from . import views

app_name = 'users_app'
urlpatterns = [
    path('login/', login, {'template_name':'users_app/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_data/', views.user_data, name='user_data'),
    path('password_change/', password_change, {'template_name':'users_app/password_change.html',
                                               'post_change_redirect':'users_app:user_data'}, name='password_change'),

]
