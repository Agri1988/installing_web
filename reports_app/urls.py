from django.urls import path, include
from . import views
from installation_app.models import Installation

app_name = 'reports_app'
urlpatterns = [
    path('month_report/<int:month>/<int:year>/', views.month_report, {'not_accepted':True}, name='month_report'),#month year report
    path('month_report/<int:month>/<int:year>/detail/', views.month_report,  {'detail': True},  name='month_report'),#month year report
    path('month_report/<int:month>/<int:year>/detail/not_accepted/', views.month_report,  {'detail': True, 'not_accepted':True},  name='month_report'),#month year report
    path('month_report/<int:month>/<int:year>/<int:employee>/', views.month_report,  name='month_report'),#month, year, employee report
    path('month_report/<int:month>/<int:year>/<int:employee>/detail/', views.month_report, {'detail': True}, name='month_report'),#month, year, employee detail report
    path('month_report/<int:month>/<int:year>/<int:employee>/detail/not_accepted/', views.month_report, {'detail': True, 'not_accepted':True}, name='month_report'),#month, year, employee detail report whith not_accepted installations
    path('month_report/', views.list_month_report,  name='list_month_report'),#create report
    path('month_report/<int:employee>/', views.list_month_report,  name='list_month_report'),#filter employee with admin
    path('working_time/', views.working_time,  name='working_time'),#workingtime list
    path('working_time/<int:ts_month>/<int:year>/<int:employee>/', views.working_time,  name='working_time'),#workingtime list
    path('create_working_time/', views.create_working_time,  name='create_working_time'),#ceate workingtime list
    path('search/', views.search, {'template':'reports_app/search_data.html',
                                   'fields':['address', 'number'],
                                   'model':Installation},  name='search'),#ceate workingtime list
]
