"""
URL configuration for ChatAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render
from django.views.static import serve
from django.urls import path, include,re_path
from .settings import STATIC_URL, STATIC_ROOT

def home_view(request):
    return render(request, 'default.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    re_path(r'^api/', include('api.urls'), name="ChatApi"),
    re_path(r'^favicon\.ico$', serve, {'document_root': STATIC_ROOT, 'path': 'favicon.ico'}),
    re_path(r'^media/', serve, {'document_root': STATIC_URL}),
]
