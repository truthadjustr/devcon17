"""codecamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from jobs.views import JobList,ArcanysJobList
from rest_framework.routers import DefaultRouter
from companies.views import CompanyAPI

api_v1_router = DefaultRouter()
api_v1_router.register(r'companies',CompanyAPI)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jobs/', JobList.as_view()),
    url(r'^ajobs/', ArcanysJobList.as_view()),
    url(r'^v1/',include(api_v1_router.urls))
]
