"""xiangqinwang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app_01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view()),
    url(r'^$', views.Login.as_view()),
    url(r'^userinfo/', views.userinfo),
    url(r'^select/', views.select),
    url(r'^regedit/', views.Regedit.as_view()),
    url(r'^look/', views.look),
    url(r'^engagement', views.engagement),
    url(r'^boy_list/', views.boy_list),
    url(r'^girl_list/', views.girl_list),
    url(r'^test/', views.test),
]
