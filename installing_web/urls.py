"""installing_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls', namespace='base_app')),
    path('mileage_account/', include('mileage_account_app.urls', namespace='mileage_account_app')),
    path('users/', include('users_app.urls', namespace='users_app')),
    path('installations/', include('installation_app.urls', namespace='installation_app')),
    path('reports/', include('reports_app.urls', namespace='reports_app')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)