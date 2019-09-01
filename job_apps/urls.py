"""Defines URL pattenrs for job_apps"""

from django.urls import path

from . import views

app_name = 'job_apps'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Application Entry Log
    path('job_log/', views.job_log, name='log')
]
