from django.urls import path, include
from . import views, forms
import datetime
app_name = 'mileage_account_app'
urlpatterns = [
    path('all_cars/', views.all_cars,  name='all_cars'),
    path('new_car/', views.detail_car,  name='new_car'),
    path('detail_car/<int:car_id>/', views.detail_car,  name='detail_car'),
    path('all_mileage_accounts/', views.all_mileage_accounts,  name='all_mileage_accounts'),
    path('all_mileage_accounts/<int:car_id>/', views.car_mileage_accounts,  name='car_mileage_accounts'),
    path('new_mileage_account/', views.detail_mileage_account,  name='new_mileage_account'),
    path('detail_mileage_account/<int:mileage_account_id>/', views.detail_mileage_account,  name='detail_mileage_account'),
    path('new_mileage_account_base_installation/<int:installation_id>/<str:date>/<int:user>/',
         views.detail_mileage_account_base_installation,  name='new_mileage_account_base_installation'),
    path('get_last_mileage/<str:car_id>/', views.get_last_mileage,  name='get_last_mileage'),
    path('all_car_refueling/', views.all_car_refueling,  name='all_car_refueling'),
    path('all_car_refueling/<int:car_id>/', views.all_car_refueling,  name='car_refueling'),
    path('new_car_refueling/', views.detail_car_refueling,  name='new_car_refueling'),
    path('detail_car_refueling/<str:car_refueling_id>/', views.detail_car_refueling,  name='detail_car_refueling'),
]
