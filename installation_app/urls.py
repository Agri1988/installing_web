from django.urls import path, include
from . import views, forms
import datetime
app_name = 'installation_app'
urlpatterns = [
    path('', views.all_installation,  name='all_installation'),
    path('<int:day>/<int:month>/<int:year>/', views.all_installation,  name='all_installation'),
    path('detail/<int:installation_id>/', views.installation_detail,  name='installation_detail'),
    path('detail/<int:installation_id>/<int:day>/<int:month>/<int:year>/', views.installation_detail,  name='add_installation'),
    path('delete/<int:installation_id>/<int:day>/<int:month>/<int:year>/', views.delete_installation,
         name='delete_installation'),
    path('add_standart', views.add_field_element,{'form':forms.InstallationStandartForm,
                                             'template':'installation_app/add_standart.html',
                                                'fieldname': 'standart'},
                                            name='add_standart'),
    path('add_type', views.add_field_element,{'form':forms.InstallationTypeForm,
                                              'template':'installation_app/add_type.html',
                                              'fieldname': 'type'},
                                                name='add_type'),
    path('delete_image/<int:installation_image_id>/', views.delete_installation_image, name='delete_image'),

]
