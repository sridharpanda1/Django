"""
URL configuration for jobs_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from jobs_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hyd-jobs/', views.hyd_jobs_info),
    path('blore-jobs/', views.blore_jobs_info),
    path('pune-jobs/', views.pune_jobs_info),
    path('bbsr-jobs/', views.bbsr_jobs_info)
]
