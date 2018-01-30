from django.urls import path, include
from . import views

app_name = 'installation_app'
urlpatterns = [
    path('', views.all_installation,  name='all_installation'),
    path('<int:day>/<int:month>/<int:year>/', views.all_installation,  name='all_installation'),
    path('detail/<int:installation_id>/', views.installation_detail,  name='installation_detail'),
    path('detail/<int:installation_id>/<int:day>/<int:month>/<int:year>/', views.installation_detail,  name='add_installation'),
    path('delete/<int:installation_id>/<int:day>/<int:month>/<int:year>/', views.delete_installation,
         name='delete_installation'),
]
