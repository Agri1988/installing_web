from django.urls import path, include
from . import views

app_name = 'reports_app'
urlpatterns = [
    path('month_report/<int:month>/<int:year>/', views.month_report,  name='month_report'),#month year report
    path('month_report/<int:month>/<int:year>/<int:employee>', views.month_report,  name='month_report'),#month, year, employee report
    path('month_report/', views.list_month_report,  name='list_month_report'),#create report
    path('month_report/<int:employee>/', views.list_month_report,  name='list_month_report'),#filter employee with admin
]
