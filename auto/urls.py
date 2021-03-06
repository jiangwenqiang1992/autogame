"""auto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from workapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from workapp.views import runyibu, clicktest, MpasSetowner, click, attack, attackboos, move, door, run, runStep

urlpatterns = [
    path('admin/', admin.site.urls),
    path('runwork/', views.runwork),
    path('yibu/', runyibu),
    path('click/', clicktest),
    path('testcheckpoint/', views.testcheckpointView),
    path('test', MpasSetowner),
    path('click', click),
    path('attack', attack),
    path('attackboos', attackboos),
    path('move', move),
    path('door', door),
    path('run', run),
    path('runStep', runStep),

]

urlpatterns += staticfiles_urlpatterns()
